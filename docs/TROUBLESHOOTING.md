# Troubleshooting

## Boot failure or recovery mode

1. Stop testing.
2. Return to fastboot.
3. Restore the saved boot image.
4. Capture the exact image/config hashes and logs.

Do not repeatedly reboot a failing image.

## Add-on crash

This release does not auto-load modules. Check:

```sh
adb shell 'cat /data/adb/modules/nh-kernel-addons/post-fs-data.sh'
adb shell 'cat /data/adb/nh-kernel-addons.log'
adb shell 'cat /proc/modules'
```

Load one module at a time and wait at least 30 seconds before loading another.

## Wi-Fi trouble

```sh
adb shell 'iw dev; iw dev wlan0 link; ip -br addr; ip route'
adb shell 'cmd wifi status'
adb shell 'dmesg | grep -iE "wlan|qcacld|cnss|firmware"'
```

A 2.4 GHz connection around −70 dBm can be usable but slow. Compare 5 GHz before blaming the kernel.

## Module refuses to load

```sh
adb shell uname -r
adb shell 'strings /data/adb/modules/nh-kernel-addons/modules/MODULE.ko | grep vermagic'
```

Never mix modules from different builds when `CONFIG_MODVERSIONS=y`.
