#!/usr/bin/env python3
"""Assemble a boot image for the rebuilt NetHunter kernel.

Inputs:
  * raw arm64 `Image` from the rebuild
  * a proven Magisk ramdisk (gzip or kernel-compatible xz)
  * the 20-DTB blob (unchanged; config changes don't affect DTBs)
  * the current working boot image, used only for its header, AVB tail and size

The optional `--neutralize-skip-initramfs` switch applies the already proven
same-length setup-string rename for defense in depth.

Header v2 layout (little endian), page size 4096, after the 8-byte magic:
   0x008 kernel_size   0x00c kernel_addr   0x010 ramdisk_size  0x014 ramdisk_addr
   0x018 second_size   0x01c second_addr   0x020 tags_addr     0x024 page_size
   0x028 header_version (2)
   1648  dtb_size (must equal len(dtb blob))
Body must stay below the AVB tail offset.
"""
import argparse
import hashlib
import os
import struct

PAGE = 4096
KERNEL_SIZE_OFF = 8
RAMDISK_SIZE_OFF = 16
DTB_SIZE_OFF = 1648


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", required=True, help="raw arm64 Image from the rebuild")
    ap.add_argument("--ramdisk", required=True, help="gzip or kernel-compatible xz ramdisk")
    ap.add_argument("--dtb", required=True, help="DTB blob (20 DTBs)")
    ap.add_argument("--base", required=True, help="current working boot image (header + AVB tail)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--neutralize-skip-initramfs", action="store_true")
    args = ap.parse_args()

    kernel = bytearray(open(args.image, "rb").read())
    ramdisk = open(args.ramdisk, "rb").read()
    blob = open(args.dtb, "rb").read()
    src = open(args.base, "rb").read()

    ks, _, rs, _, _, _, _, page, hv, _ = struct.unpack("<10I", src[8:48])
    assert page == PAGE, f"unexpected page size {page}"
    assert hv == 2, f"unexpected header version {hv}"
    vboff = struct.unpack(">Q", src[-64 + 12:-64 + 20])[0]

    # sanity: raw Image, not Image.gz
    assert kernel[:2] != b"\x1f\x8b", "Image is gzip-compressed; pass the raw arm64 Image"
    if ramdisk[:2] == b"\x1f\x8b":
        ramdisk_comp = "gzip"
    elif ramdisk[:6] == b"\xfd7zXZ\x00":
        ramdisk_comp = "xz"
    else:
        raise AssertionError("ramdisk is neither gzip nor xz")

    if args.neutralize_skip_initramfs:
        old = b"skip_initramfs"
        new = b"skip_initramfZ"
        hits = [i for i in range(len(kernel)) if kernel.startswith(old, i)]
        assert len(hits) == 1, f"expected one skip_initramfs setup string, got {hits}"
        kernel[hits[0]:hits[0] + len(old)] = new
        print(f"  neutralized skip_initramfs setup string at 0x{hits[0]:x}")
    old_dtb = struct.unpack_from("<I", src, DTB_SIZE_OFF)[0]
    print(f"  base header: page={page} v={hv} kernel={ks:,} ramdisk={rs:,} dtb={old_dtb:,}")
    print(f"  avb tail at {vboff:,}, image total {len(src):,}")

    hdr = bytearray(src[:PAGE])
    struct.pack_into("<I", hdr, KERNEL_SIZE_OFF, len(kernel))
    struct.pack_into("<I", hdr, RAMDISK_SIZE_OFF, len(ramdisk))
    struct.pack_into("<I", hdr, DTB_SIZE_OFF, len(blob))

    img = bytes(hdr)
    img += bytes(kernel) + b"\x00" * ((-len(kernel)) % PAGE)
    img += ramdisk + b"\x00" * ((-len(ramdisk)) % PAGE)
    img += blob
    body = len(img)
    assert body <= vboff, f"body {body:,} B overruns AVB tail at {vboff:,} B"
    img += b"\x00" * (vboff - body) + src[vboff:]
    img += b"\x00" * (len(src) - len(img))
    assert len(img) == len(src), "output size changed"

    with open(args.out, "wb") as fh:
        fh.write(img)

    print(f"  wrote {args.out}")
    print(f"    kernel  {len(kernel):>10,} B")
    print(f"    ramdisk {len(ramdisk):>10,} B ({ramdisk_comp})")
    print(f"    dtb     {len(blob):>10,} B (20 DTBs, unchanged)")
    print(f"    body    {body:>10,} B   (headroom {vboff - body:,} B)")
    print(f"    total   {len(img):>10,} B")
    print(f"    sha256  {hashlib.sha256(img).hexdigest()}")


if __name__ == "__main__":
    main()
