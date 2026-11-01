#!/bin/sh
# Collect the rebuilt out-of-tree modules from the build container and refresh
# the nh-kernel-addons Magisk module payload.
#
# Every module must be replaced together: the new config (DEBUG_FS, KPROBES, ...)
# changes symbol CRCs, so an old .ko against the new kernel would fail its
# modversions check and refuse to load.
set -eu

HERE=$(cd "$(dirname "$0")" && pwd)
STAGE=${STAGE:-$HERE/modules-staged}
MODDIR=${MODDIR:-$HERE/nh-kernel-addons-build9}
CONTAINER=nhbuild
KSRC=/srv/k2

# Dependency order.  Keep this in sync with post-fs-data.sh.
MODS="xxhash zstd_decompress squashfs usb_wwan option slcan vxcan hlcan ems_usb kvaser_usb gspca_main 8188eu ifb mac80211_hwsim binfmt_misc cifs isofs ntfs udf sch_netem sch_tbf"

rm -rf "$STAGE"
mkdir -p "$STAGE"

echo "== pulling modules from $CONTAINER:$KSRC/out"
for m in $MODS; do
    src=$(podman exec "$CONTAINER" sh -c "find $KSRC/out -name '$m.ko' -type f | head -1")
    if [ -z "$src" ]; then
        echo "  MISSING: $m.ko" >&2
        exit 1
    fi
    podman cp "$CONTAINER:$src" "$STAGE/$m.ko"
    printf '  %-12s %8s B  %s\n' "$m.ko" "$(wc -c < "$STAGE/$m.ko" | tr -d ' ')" "${src#$KSRC/out/}"
done

echo "== vermagic check (must all match the new kernel release)"
for f in "$STAGE"/*.ko; do
    v=$(strings "$f" | grep -m1 '^vermagic=')
    printf '  %-14s %s\n' "$(basename "$f")" "$v"
done

echo "== updating $MODDIR/modules"
rm -rf "$MODDIR/modules"
mkdir -p "$MODDIR/modules"
cp "$STAGE"/*.ko "$MODDIR/modules/"

echo "== repacking module zip"
( cd "$MODDIR" && zip -qr "$HERE/nh-kernel-addons-rebuilt.zip" . -x '.*' )
sha256sum "$HERE/nh-kernel-addons-rebuilt.zip" 2>/dev/null || shasum -a 256 "$HERE/nh-kernel-addons-rebuilt.zip"
echo "done"
