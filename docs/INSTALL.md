# Installation and recovery

## Before you begin

- Confirm the device model, ROM and Android version.
- Confirm the boot partition is exactly 100,663,296 bytes.
- Ensure fastboot and root access work.
- Save the current boot image off-device.
- Keep a second cable/port available for recovery.

## Verify downloads

```sh
shasum -a 256 -c SHA256SUMS
```

Do not flash if any checksum fails.

## Flash

The tested target is `boot_b`. Confirm the active slot and partition name first.

```sh
fastboot getvar current-slot
fastboot flash boot_b boot-nh-advanced-build11-gzip.img
fastboot reboot
```

After Android starts:

```sh
adb shell uname -a
adb shell su -c 'magisk -v'
```

Install `nh-kernel-addons-build11-safe-fixed.zip` through Magisk. The module intentionally does not insert drivers during boot.

## Recovery

If Android does not boot, return to fastboot and restore the boot image you backed up. Do not erase userdata as a first response to a kernel failure.
