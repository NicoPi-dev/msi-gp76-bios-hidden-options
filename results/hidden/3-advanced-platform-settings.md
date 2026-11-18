# Advanced > Platform Settings

Category: **Hidden - MSI advanced menu** - 78 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > Platform Settings | Secondary Configuration Rework Option | Disabled (0x0) \| x4 PCIe Slot (0x1) \| TBT AIC (0x2) | Disabled | `Setup` @ `0x676` (1) |
| Advanced > Platform Settings | Secondary Configuration Rework Option For TBT | TBT BP Onboard Enable (0x0) \| TBT FP AIC Enable (0x1) | TBT BP Onboard Enable | `Setup` @ `0x676` (1) |
| Advanced > Platform Settings | UCSI Retry Mechanism | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x533` (1) |
| Advanced > Platform Settings | PS2 Keyboard and Mouse | Enabled (0x1) \| Disabled (0x0) | Enabled | `Setup` @ `0x38f` (1) |
| Advanced > Platform Settings | Power Loss Notification Feature | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x66f` (1) |
| Advanced > Platform Settings | Charging Method | Normal Charging (0x0) \| Fast Charging (0x1) | Normal Charging | `Setup` @ `0x4f3` (1) |
| Advanced > Platform Settings | Pmic Vcc IO Level | Disabled (0x7) \| 1.05V (0x0) \| 1.071V (0x1) \| 1.023V (0x2) \| 0.997V (0x3) \| 0.850V (0x4) \| 0.900V (0x5) \| 0.950V (0x6) | Disabled | `Setup` @ `0x39d` (1) |
| Advanced > Platform Settings | Pmic Vddq Level | Disabled (0x8) \| 0 (0x0) \| 1 (0x1) \| 2 (0x2) \| 3 (0x3) \| 4 (0x4) \| 5 (0x5) \| 6 (0x6) \| 7 (0x7) | Disabled | `Setup` @ `0x39e` (1) |
| Advanced > Platform Settings | Pmic SlpS0 VM Support | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x4e4` (1) |
| Advanced > Platform Settings | Enable FFU Support | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x49a` (1) |
| Advanced > Platform Settings | Delay to wait for WWAN device to be ready before SAR reset. | 0 … 255 (step 1) | 8 | `Setup` @ `0x4e9` (1) |
| Advanced > Platform Settings | Type-C BSSB Mode | Mode 0 (0x0) \| Mode 1 (0x1) | Mode 1 | `Setup` @ `0x4eb` (1) |
| Advanced > Platform Settings | Enable PowerMeter | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x529` (1) |
| Advanced > Platform Settings | HID Event Filter Driver | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x4e3` (1) |
| Advanced > Platform Settings | HEBC value | 0 … 4294967295 (step 1) | 144371 | `Setup` @ `0x4e5` (4) |
| Advanced > Platform Settings | Pcie Slot 1 to x4 Mode Rework | Enabled (0x1) \| Disabled (0x0) | Disabled | `Setup` @ `0x525` (1) |
| Advanced > Platform Settings | PCIe x16 slot GSPI0_CLK Rework | Enabled (0x1) \| Disabled (0x0) | Disabled | `Setup` @ `0x531` (1) |
| Advanced > Platform Settings | PCIe x16 slot GSXDOUT Rework | Enabled (0x1) \| Disabled (0x0) | Disabled | `Setup` @ `0x532` (1) |
| Advanced > Platform Settings | DGPU Power Enable | Enabled (0x1) \| Disabled (0x0) | Disabled | `Setup` @ `0x527` (1) |
| Advanced > Platform Settings | System Time and Alarm Source | ACPI Time and Alarm Device (0x0) \| Legacy RTC (0x1) | Legacy RTC | `Setup` @ `0x535` (1) |
| Advanced > Platform Settings | Intel Trusted Device Setup Boot | Enabled (0x1) \| Disabled (0x0) | Disabled | `Setup` @ `0x66e` (1) |
| Advanced > Platform Settings | Support PEG Bifurcation Card | Enabled (0x1) \| Disabled (0x0) | Disabled | `Setup` @ `0x67b` (1) |
| Advanced > Platform Settings > VTIO | Enable VTIO Support | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x4ec` (1) |
| Advanced > Platform Settings > VTIO | Expose ISP SDEV Entry | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x4ee` (1) |
| Advanced > Platform Settings > VTIO | Number of Sensor Entries | 0 … 2 (step 0) | 90 | `Setup` @ `0x4fe` (2) |
| Advanced > Platform Settings > VTIO | Flags | 0 … 1 (step 0) | 90 | `Setup` @ `0x671` (1) |
| Advanced > Platform Settings > VTIO | Sensor Entry 1 | 0 … 65535 (step 0) | 90 | `Setup` @ `0x508` (2) |
| Advanced > Platform Settings > VTIO | Sensor Entry 2 | 0 … 65535 (step 0) | 90 | `Setup` @ `0x512` (2) |
| Advanced > Platform Settings > VTIO | Expose HECI SDEV Entry | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x4f0` (1) |
| Advanced > Platform Settings > VTIO | Number of Sensor Entries | 0 … 2 (step 0) | 90 | `Setup` @ `0x500` (2) |
| Advanced > Platform Settings > VTIO | Flags | 0 … 1 (step 0) | 90 | `Setup` @ `0x672` (1) |
| Advanced > Platform Settings > VTIO | Sensor Entry 1 | 0 … 65535 (step 0) | 90 | `Setup` @ `0x50a` (2) |
| Advanced > Platform Settings > VTIO | Sensor Entry 2 | 0 … 65535 (step 0) | 90 | `Setup` @ `0x514` (2) |
| Advanced > Platform Settings > VTIO | Expose SPI1 Dev 1E Fun 2 SDEV Entry | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x4f1` (1) |
| Advanced > Platform Settings > VTIO | Number of Sensor Entries | 0 … 2 (step 0) | 90 | `Setup` @ `0x502` (2) |
| Advanced > Platform Settings > VTIO | Flags | 0 … 1 (step 0) | 90 | `Setup` @ `0x673` (1) |
| Advanced > Platform Settings > VTIO | Sensor Entry 1 | 0 … 65535 (step 0) | 90 | `Setup` @ `0x50c` (2) |
| Advanced > Platform Settings > VTIO | Sensor Entry 2 | 0 … 65535 (step 0) | 90 | `Setup` @ `0x516` (2) |
| Advanced > Platform Settings > VTIO | Expose SPI2 Dev 1E Fun 3 SDEV Entry | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x4f2` (1) |
| Advanced > Platform Settings > VTIO | Number of Sensor Entries | 0 … 2 (step 0) | 90 | `Setup` @ `0x504` (2) |
| Advanced > Platform Settings > VTIO | Flags | 0 … 1 (step 0) | 90 | `Setup` @ `0x674` (1) |
| Advanced > Platform Settings > VTIO | Sensor Entry 1 | 0 … 65535 (step 0) | 90 | `Setup` @ `0x50e` (2) |
| Advanced > Platform Settings > VTIO | Sensor Entry 2 | 0 … 65535 (step 0) | 90 | `Setup` @ `0x518` (2) |
| Advanced > Platform Settings > VTIO | Expose XHCI SDEV Entry | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x4ef` (1) |
| Advanced > Platform Settings > VTIO | Number of USB Devices | 1 … 2 (step 0) | 90 | `Setup` @ `0x538` (1) |
| Advanced > Platform Settings > VTIO | Flags | 0 … 1 (step 0) | 90 | `Setup` @ `0x675` (1) |
| Advanced > Platform Settings > VTIO | Attributes | 0 … 255 (step 0) | 90 | `Setup` @ `0x539` (1) |
| Advanced > Platform Settings > VTIO | Root Port Number | 0 … 255 (step 0) | 90 | `Setup` @ `0x53b` (1) |
| Advanced > Platform Settings > VTIO | VID | 0 … 65535 (step 0) | 90 | `Setup` @ `0x53d` (2) |
| Advanced > Platform Settings > VTIO | PID | 0 … 65535 (step 0) | 90 | `Setup` @ `0x541` (2) |
| Advanced > Platform Settings > VTIO | Revision | 0 … 65535 (step 0) | 90 | `Setup` @ `0x545` (2) |
| Advanced > Platform Settings > VTIO | Interface Number | 0 … 255 (step 0) | 90 | `Setup` @ `0x549` (1) |
| Advanced > Platform Settings > VTIO | Class | 0 … 255 (step 0) | 90 | `Setup` @ `0x54b` (1) |
| Advanced > Platform Settings > VTIO | Subclass | 0 … 255 (step 0) | 90 | `Setup` @ `0x54d` (1) |
| Advanced > Platform Settings > VTIO | Protocol | 0 … 255 (step 0) | 90 | `Setup` @ `0x54f` (1) |
| Advanced > Platform Settings > VTIO | ACPI Path String Offset | 0 … 65535 (step 0) | 90 | `Setup` @ `0x551` (2) |
| Advanced > Platform Settings > VTIO | ACPI Path String Length | 0 … 65535 (step 0) | 90 | `Setup` @ `0x555` (2) |
| Advanced > Platform Settings > VTIO | Firmware Hash [255:192] | 0 … 18446744073709551615 (step 1) | 0 | `Setup` @ `0x571` (8) |
| Advanced > Platform Settings > VTIO | Firmware Hash [191:128] | 0 … 18446744073709551615 (step 1) | 0 | `Setup` @ `0x569` (8) |
| Advanced > Platform Settings > VTIO | Firmware Hash [127:64] | 0 … 18446744073709551615 (step 1) | 0 | `Setup` @ `0x561` (8) |
| Advanced > Platform Settings > VTIO | Firmware Hash [63:0] | 0 … 18446744073709551615 (step 1) | 0 | `Setup` @ `0x559` (8) |
| Advanced > Platform Settings > VTIO | ACPI Path Name |  |  | `Setup` @ `0x599` (1) |
| Advanced > Platform Settings > VTIO | Attributes | 0 … 255 (step 0) | 90 | `Setup` @ `0x53a` (1) |
| Advanced > Platform Settings > VTIO | Root Port Number | 0 … 255 (step 0) | 90 | `Setup` @ `0x53c` (1) |
| Advanced > Platform Settings > VTIO | VID | 0 … 65535 (step 0) | 90 | `Setup` @ `0x53f` (2) |
| Advanced > Platform Settings > VTIO | PID | 0 … 65535 (step 0) | 90 | `Setup` @ `0x543` (2) |
| Advanced > Platform Settings > VTIO | Revision | 0 … 65535 (step 0) | 90 | `Setup` @ `0x547` (2) |
| Advanced > Platform Settings > VTIO | Interface Number | 0 … 255 (step 0) | 90 | `Setup` @ `0x54a` (1) |
| Advanced > Platform Settings > VTIO | Class | 0 … 255 (step 0) | 90 | `Setup` @ `0x54c` (1) |
| Advanced > Platform Settings > VTIO | Subclass | 0 … 255 (step 0) | 90 | `Setup` @ `0x54e` (1) |
| Advanced > Platform Settings > VTIO | Protocol | 0 … 255 (step 0) | 90 | `Setup` @ `0x550` (1) |
| Advanced > Platform Settings > VTIO | ACPI Path String Offset | 0 … 65535 (step 0) | 90 | `Setup` @ `0x553` (2) |
| Advanced > Platform Settings > VTIO | ACPI Path String Length | 0 … 65535 (step 0) | 90 | `Setup` @ `0x557` (2) |
| Advanced > Platform Settings > VTIO | Firmware Hash [255:192] | 0 … 18446744073709551615 (step 1) | 0 | `Setup` @ `0x591` (8) |
| Advanced > Platform Settings > VTIO | Firmware Hash [191:128] | 0 … 18446744073709551615 (step 1) | 0 | `Setup` @ `0x589` (8) |
| Advanced > Platform Settings > VTIO | Firmware Hash [127:64] | 0 … 18446744073709551615 (step 1) | 0 | `Setup` @ `0x581` (8) |
| Advanced > Platform Settings > VTIO | Firmware Hash [63:0] | 0 … 18446744073709551615 (step 1) | 0 | `Setup` @ `0x579` (8) |
| Advanced > Platform Settings > VTIO | ACPI Path Name |  |  | `Setup` @ `0x5fb` (1) |
