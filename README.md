# Kali NetHunter kernel — OnePlus 7 Pro / LOS 23.2

This is a tested build for the OnePlus 7 Pro (GM1911) running LineageOS 23.2 / Android 16.

## Tested release

- Kernel: `4.14.357-v0lk3n-SM8150_OP7Serie-LOS_23.2+`
- Build: build11, Clang/LLD 21.1.8, arm64
- Boot image: v2 header, 4096-byte pages, 20-DTB blob
- `DEBUG_FS` is intentionally disabled to keep the raw kernel within the proven gzip boot budget.
- KPROBES, PSTORE/ramoops, UVC gadget, RD_XZ/RD_LZ4, and the requested filesystem/network modules are enabled.
- Add-on modules are installed but never auto-loaded. Use the module's `load-on-demand.sh` as root for individual features.

## Important warnings

This is not a universal OnePlus 7 Pro image. Do not flash it on another model, ROM, slot layout, or DTB set without rebuilding and testing. Make a boot-partition backup first and keep a working restore image available. The maintainer's tested rollback image is not included in this release bundle.

The image contains a Magisk-compatible ramdisk but no personal data or keys. Users should install their own Magisk setup where appropriate.

## Installation

1. Verify the SHA-256 values in `SHA256SUMS`.
2. Confirm the device model, ROM, slot, and boot partition size.
3. Save the current boot image.
4. Flash only the matching boot partition with fastboot, then reboot.
5. Install the safe add-on ZIP through Magisk. Modules remain on-demand after boot.

If Android does not boot, return to fastboot and restore the saved boot image immediately.

## Source and licensing

The source is based on `V0lk3n/nethunter_kernel_oneplus_sm8150`, branch `nethunter-lineage-23.2`, with the documented build configuration and compatibility fixes. Publish the corresponding source commit, configuration, patches, and build instructions alongside these binaries. Preserve all upstream GPL and third-party notices; binaries alone are not a substitute for the required source offer.

