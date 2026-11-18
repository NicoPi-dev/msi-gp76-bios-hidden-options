# Advanced > AMT Configuration

Category: **Hidden - MSI advanced menu** - 18 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > AMT Configuration | USB Provisioning of AMT | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x01f` (1) |
| Advanced > AMT Configuration > ASF Configuration | PET Progress | Disabled (0x0) \| Enabled (0x1) | Enabled | `MeSetup` @ `0x020` (1) |
| Advanced > AMT Configuration > ASF Configuration | WatchDog | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x023` (1) |
| Advanced > AMT Configuration > ASF Configuration | OS Timer | 0 … 65535 (step 1) | 0 | `MeSetup` @ `0x024` (2) |
| Advanced > AMT Configuration > ASF Configuration | BIOS Timer | 0 … 65535 (step 1) | 0 | `MeSetup` @ `0x026` (2) |
| Advanced > AMT Configuration > ASF Configuration | ASF Sensors Table | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x022` (1) |
| Advanced > AMT Configuration > CIRA Configuration | Activate Remote Assistance Process | Disabled (0) \| Enabled (1) | Disabled | `MeSetup` @ `0x01d` (1) |
| Advanced > AMT Configuration > CIRA Configuration | CIRA Timeout | 0 … 255 (step 1) | 0 | `MeSetup` @ `0x01e` (1) |
| Advanced > AMT Configuration > MEBx Resolution Settings | Non-UI Mode Resolution | Auto (0x0) \| 80x25 (0x1) \| 100x31 (0x2) | Auto | `MeSetup` @ `0x028` (1) |
| Advanced > AMT Configuration > MEBx Resolution Settings | UI Mode Resolution | Auto (0x0) \| 80x25 (0x1) \| 100x31 (0x2) | Auto | `MeSetup` @ `0x029` (1) |
| Advanced > AMT Configuration > MEBx Resolution Settings | Graphics Mode Resolution | Auto (0x0) \| 640x480 (0x1) \| 800x600 (0x2) \| 1024x768 (0x3) | Auto | `MeSetup` @ `0x02a` (1) |
| Advanced > AMT Configuration > OEM Flags Settings | MEBx hotkey Pressed | Disabled (0) \| Enabled (1) | Disabled | `MeSetup` @ `0x018` (1) |
| Advanced > AMT Configuration > OEM Flags Settings | MEBx Selection Screen | Disabled (0) \| Enabled (1) | Disabled | `MeSetup` @ `0x019` (1) |
| Advanced > AMT Configuration > OEM Flags Settings | Hide Unconfigure ME Confirmation Prompt | Disabled (0) \| Enabled (1) | Disabled | `MeSetup` @ `0x01a` (1) |
| Advanced > AMT Configuration > OEM Flags Settings | MEBx OEM Debug Menu Enable | Disabled (0) \| Enabled (1) | Disabled | `MeSetup` @ `0x01b` (1) |
| Advanced > AMT Configuration > OEM Flags Settings | Unconfigure ME | Disabled (0) \| Enabled (1) | Disabled | `MeSetup` @ `0x01c` (1) |
| Advanced > AMT Configuration > Secure Erase Configuration | Secure Erase mode | Simulated (0x0) \| Real (0x1) | Simulated | `Setup` @ `0x4e1` (1) |
| Advanced > AMT Configuration > Secure Erase Configuration | Force Secure Erase | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x4e2` (1) |
