# Boot

Category: **Hidden - MSI advanced menu** - 12 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Boot | Setup Prompt Timeout | 1 … 65535 (step 1) | 1 | `Timeout` @ `0x000` (2) |
| Boot | Quiet Boot | Disabled (0) \| Enabled (1) | 1 | `AMITSESetup` @ `0x050` (1) |
| Boot | Quiet Boot | Disabled (0) \| Enabled (1) | 1 | `AMITSESetup` @ `0x050` (1) |
| Boot | SATA Support | Last Boot SATA Devices Only (0x0) \| All SATA Devices (0x1) | All SATA Devices | `Setup` @ `0x67e` (1) |
| Boot | NVMe Support | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x684` (1) |
| Boot | VGA Support | Auto (0x0) \| EFI Driver (0x1) | EFI Driver | `Setup` @ `0x67f` (1) |
| Boot | USB Support | Disabled (0x0) \| Full Initial (0x1) \| Partial Initial (0x2) | Full Initial | `Setup` @ `0x680` (1) |
| Boot | PS2 Devices Support | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x681` (1) |
| Boot | Network Stack Driver Support | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x683` (1) |
| Boot | Redirection Support | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x682` (1) |
| Boot | Driver Option #%d |  (0x0) \|  (0x1) |  | `DriverOrder` @ `0x000` (2) |
| Boot | Boot mode select | LEGACY (0x0) \| UEFI (0x1) | UEFI | `Setup` @ `0x74e` (1) |
