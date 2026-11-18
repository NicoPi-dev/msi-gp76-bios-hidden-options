# Advanced

Category: **Hidden - MSI advanced menu** - 4 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced | Firmware Configuration | Ignore Policy Update (0x0) \| Production (0x1) \| Test (0x2) | Test | `Setup` @ `0x002` (1) |
| Advanced | Type C Support | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Disabled | `Setup` @ `0x52c` (1) |
| Advanced | Test function 1 | Disabled (0) \| Enabled (1) | 1 | `Setup` @ `0x72b` (1) |
| Advanced | MSI VGA MODE | MS-Hybrid MODE (0x0) \| Discrete MODE (0x1) | MS-Hybrid MODE | `Setup` @ `0x731` (1) |
