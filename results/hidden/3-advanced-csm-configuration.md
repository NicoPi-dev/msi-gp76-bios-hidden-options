# Advanced > CSM Configuration

Category: **Hidden - MSI advanced menu** - 10 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > CSM Configuration | CSM Support | Disabled (0x0) \| Enabled (0x1) | 0 | `Setup` @ `0x743` (1) |
| Advanced > CSM Configuration | GateA20 Active | Upon Request (0x0) \| Always (0x1) | Upon Request | `Setup` @ `0x748` (1) |
| Advanced > CSM Configuration | Option ROM Messages | Force BIOS (0x1) \| Keep Current (0x0) | Force BIOS | `Setup` @ `0x744` (1) |
| Advanced > CSM Configuration | INT19 Trap Response | Immediate (0x1) \| Postponed (0x0) | Immediate | `Setup` @ `0x745` (1) |
| Advanced > CSM Configuration | HDD Connection Order | Adjust (0x0) \| Keep (0x1) | Adjust | `Setup` @ `0x747` (1) |
| Advanced > CSM Configuration | Boot option filter | UEFI and Legacy (0x0) \| Legacy only (0x1) \| UEFI only (0x2) | 2 | `Setup` @ `0x749` (1) |
| Advanced > CSM Configuration | Network | Do not launch (0x0) \| UEFI (0x1) \| Legacy (0x2) | 0 | `Setup` @ `0x74a` (1) |
| Advanced > CSM Configuration | Storage | Do not launch (0x0) \| UEFI (0x1) \| Legacy (0x2) | 1 | `Setup` @ `0x74b` (1) |
| Advanced > CSM Configuration | Video | Do not launch (0x0) \| UEFI (0x1) \| Legacy (0x2) | 1 | `Setup` @ `0x74c` (1) |
| Advanced > CSM Configuration | Other PCI devices | Do not launch (0x0) \| UEFI (0x1) \| Legacy (0x2) | UEFI | `Setup` @ `0x74d` (1) |
