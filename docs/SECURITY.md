# Security and release policy

This project modifies a boot image and loads kernel modules with root privileges. A malformed image or incompatible module can make a device unbootable.

Release rules:

- Publish checksums for every binary.
- Keep personal ramdisks, Magisk databases, keys, device dumps and backups private.
- Never enable automatic loading for experimental drivers without a tested rollback.
- Test on the exact model/ROM/slot layout named in the release.
- Preserve upstream GPL and third-party notices.
- Report reproducible crashes with image hash, config hash, model and sanitized logs.

Do not publish serial numbers, credentials, modem data or private crash dumps.
