# Advanced > ACPI Settings

Category: **Hidden - MSI advanced menu** - 4 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > ACPI Settings | Enable ACPI Auto Configuration | Disabled (0) \| Enabled (1) | 0 | `Setup` @ `0x6a7` (1) |
| Advanced > ACPI Settings | Enable Hibernation | Disabled (0) \| Enabled (1) | 1 | `Setup` @ `0x6aa` (1) |
| Advanced > ACPI Settings | ACPI Sleep State | Suspend Disabled (0x0) \| S3 (Suspend to RAM) (0x2) | S3 (Suspend to RAM) | `Setup` @ `0x6a8` (2) |
| Advanced > ACPI Settings | S3 Video Repost | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6ab` (1) |
