# Reproducible build notes

## Upstream

Source: `V0lk3n/nethunter_kernel_oneplus_sm8150`  
Branch: `nethunter-lineage-23.2`  
Architecture: `arm64`

The authoritative source was built inside a case-sensitive Ubuntu 24.04 arm64 container. Building this tree directly on macOS APFS can collapse case-differing files.

## Toolchain

- Clang/LLD/LLVM 21.1.8 from apt.llvm.org
- aarch64 binutils
- bison, flex, libssl, bc, kmod, cpio, rsync, dtc, libelf and ncurses
- Podman arm64 container with an ext4 source volume

## Configuration

Use `config-build11` as the exact reference configuration. Important choices:

- `CONFIG_DEBUG_FS=n` to fit the proven gzip ramdisk budget
- `CONFIG_INITRAMFS_IGNORE_SKIP_FLAG=n`; the assembler applies the proven setup-string neutralization
- `CONFIG_KPROBES=y`
- PSTORE/ramoops and UVC gadget enabled
- Heavy optional features built as modules

## Image assembly

`build-boot-image.py` takes a raw `Image`, a gzip/xz ramdisk, the device DTB blob and a known-good v2 base image. It checks page size, header version, AVB-tail headroom and final size.

```sh
python3 build-boot-image.py \
  --image Image-build11 --ramdisk ramdisk.cpio.gz \
  --dtb dtb_blob.bin --base known-good-boot.img \
  --out boot-nh-advanced-build11-gzip.img \
  --neutralize-skip-initramfs
```

The DTB blob is device-specific.
