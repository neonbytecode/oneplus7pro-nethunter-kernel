# Promotion kit

Use the canonical project link in every post:

<https://github.com/neonbytecode/oneplus7pro-nethunter-kernel>

## Short announcement

> **NetHunter Cyberdeck Kernel for OnePlus 7 Pro**
>
> Build11 for GM1911 on LineageOS 23.2 / Android 16. Magisk-compatible boot image, 21 safe on-demand kernel modules, PSTORE/KPROBES/UVC support, and documented rollback. Wi-Fi and normal boot were tested; add-ons never auto-load.
>
> Download, verify SHA256, and read the recovery guide before flashing:
> <https://github.com/neonbytecode/oneplus7pro-nethunter-kernel>

## XDA / forum post

**Title:** `[KERNEL][NETHUNTER][LOS 23.2] OnePlus 7 Pro Cyberdeck Kernel — Build11`

**Post:**

This is a device- and ROM-specific Kali NetHunter kernel for the OnePlus 7 Pro GM1911 running LineageOS 23.2 / Android 16.

Highlights:

- arm64 4.14.357 kernel, Clang/LLD 21.1.8
- Magisk-compatible build11 boot image
- 21 modules installed for on-demand use; no early-boot auto-loading
- PSTORE/ramoops, KPROBES, UVC gadget, RD_XZ/RD_LZ4
- CIFS, NTFS, ISO9660, UDF, SquashFS, IFB, NETEM, TBF, USB serial and CAN modules
- Verified rollback image and SHA256 manifest

Read the compatibility and installation guide before flashing. Please report the exact model, ROM build, slot, module command and recovery logs with any issue.

## Reddit / chat version

OnePlus 7 Pro NetHunter users: I published a tested LineageOS 23.2 / Android 16 kernel with safe, on-demand modules. It includes the documented boot image, Magisk module, checksums, rollback instructions and troubleshooting guide. This is **not** a universal kernel—GM1911 + the listed ROM only.

Project: <https://github.com/neonbytecode/oneplus7pro-nethunter-kernel>

## Launch checklist

- Link to the GitHub repository, not a re-upload or shortened URL.
- Say explicitly that this is GM1911 + LineageOS 23.2 / Android 16 specific.
- Include the SHA256 verification and rollback instructions.
- Do not promise internal Wi-Fi monitor mode; use an external compatible adapter where required.
- Ask users to star the repository only if they find it useful; do not spam or mass-post duplicate submissions.
- Keep support requests in GitHub Issues so logs and fixes remain searchable.

## Good channels

- XDA OnePlus 7/7 Pro/7T/7T Pro cross-device kernel development
- Kali Linux community forums, in a NetHunter/device-development thread
- Relevant OnePlus 7 Pro and Kali Linux Reddit communities, following their self-promotion rules
- NetHunter community channels, after checking whether device-specific kernels are accepted

The official Kali documentation describes NetHunter as a community-developed open-source project and points users to the Kali community forums for support. The official NetHunter kernel/device tables are the right place to investigate upstream listing requirements before submitting a device entry.
