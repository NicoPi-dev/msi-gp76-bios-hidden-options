# Advanced > Network Stack Configuration

Category: **Hidden - MSI advanced menu** - 7 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > Network Stack Configuration | Network Stack | Disabled (0x0) \| Enabled (0x1) | Disabled | `NetworkStackVar` @ `0x000` (1) |
| Advanced > Network Stack Configuration | Ipv4 PXE Support | Disabled (0x0) \| Enabled (0x1) | Enabled | `NetworkStackVar` @ `0x001` (1) |
| Advanced > Network Stack Configuration | Ipv4 HTTP Support | Disabled (0x0) \| Enabled (0x1) | Disabled | `NetworkStackVar` @ `0x006` (1) |
| Advanced > Network Stack Configuration | Ipv6 PXE Support | Disabled (0x0) \| Enabled (0x1) | Enabled | `NetworkStackVar` @ `0x002` (1) |
| Advanced > Network Stack Configuration | Ipv6 HTTP Support | Disabled (0x0) \| Enabled (0x1) | Disabled | `NetworkStackVar` @ `0x007` (1) |
| Advanced > Network Stack Configuration | PXE boot wait time | 0 … 5 (step 1) | 0 | `NetworkStackVar` @ `0x004` (1) |
| Advanced > Network Stack Configuration | Media detect count | 1 … 50 (step 1) | 1 | `NetworkStackVar` @ `0x005` (1) |
