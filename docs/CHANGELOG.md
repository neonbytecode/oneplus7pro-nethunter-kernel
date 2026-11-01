# Changelog

## build11 — current

- Disabled `DEBUG_FS` to fit the proven gzip Magisk ramdisk.
- Disabled `INITRAMFS_IGNORE_SKIP_FLAG`; retained the proven setup-string neutralization.
- Retained KPROBES, PSTORE/ramoops, UVC gadget, RD_XZ/RD_LZ4 and optional modules.
- Replaced early module autoloading with explicit on-demand loading.
- Fixed dependency handling in the on-demand loader.
- Verified normal boot, Magisk, Wi-Fi and controlled module loading on GM1911 / LOS 23.2.

## build10

- First gzip-sized kernel after disabling debugfs.
- Rejected after normal boot entered recovery; superseded by build11.
