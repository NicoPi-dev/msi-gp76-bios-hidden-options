# Advanced > Intel ICC

Category: **Hidden - MSI advanced menu** - 7 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > Intel ICC | ICC/OC Watchdog Timer | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x4d6` (1) |
| Advanced > Intel ICC | ICC Profile | 0 … 15 (step 1) | 0 | `IccAdvancedSetupDataVar` @ `0x006` (1) |
| Advanced > Intel ICC | ICC PLL Shutdown | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x4db` (1) |
| Advanced > Intel ICC | Clock Frequency | 0 … 65535 (step 1) | 0 | `IccAdvancedSetupDataVar` @ `0x000` (2) |
| Advanced > Intel ICC | Bclk Change Permanent | Enabled (0x1) \| Disabled (0x0) | Enabled | `SaSetup` @ `0x205` (1) |
| Advanced > Intel ICC | Bclk Change w/o Reset | Real Time change (0x0) \| Permanent, no warm reset (0x1) | Real Time change | `SaSetup` @ `0x206` (1) |
| Advanced > Intel ICC | Spread % | 0 … 255 (step 1) | 0 | `IccAdvancedSetupDataVar` @ `0x002` (1) |
