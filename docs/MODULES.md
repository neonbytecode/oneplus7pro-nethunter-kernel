# Module catalog

The Magisk module contains 21 `.ko` files built against the exact build11 ABI. Automatic loading is disabled because early loading of experimental/virtual drivers caused instability during development.

## On-demand loader

```sh
su -c 'sh /data/adb/modules/nh-kernel-addons/load-on-demand.sh MODULE [MODULE ...]'
```

Dependencies are handled for `squashfs` (`xxhash`, `zstd_decompress`) and `option` (`usb_wwan`).

| Module | Capability |
| --- | --- |
| `squashfs` | SquashFS mounts |
| `cifs` | SMB/CIFS mounts |
| `isofs` | ISO9660 mounts |
| `ntfs` | NTFS mounts |
| `udf` | UDF filesystems |
| `binfmt_misc` | Additional executable formats |
| `ifb` | Intermediate Functional Block devices |
| `sch_netem` | Network delay/loss/reordering |
| `sch_tbf` | Token Bucket Filter shaping |
| `usb_wwan`, `option` | USB modem/serial devices |
| `slcan`, `vxcan`, `hlcan`, `ems_usb`, `kvaser_usb` | SocketCAN adapters |
| `gspca_main` | USB camera framework |
| `8188eu` | External RTL8188EU Wi-Fi adapter |
| `mac80211_hwsim` | Virtual simulated Wi-Fi radios |

Do not load `mac80211_hwsim` while diagnosing internal Qualcomm Wi-Fi. It creates virtual PHYs.
