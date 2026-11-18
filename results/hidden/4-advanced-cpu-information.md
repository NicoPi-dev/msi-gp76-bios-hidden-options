# Advanced > CPU Information

Category: **Hidden - permanently** - 3 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > CPU Information | Maximum Supported PRMRR Size | 0 … 4294967295 (step 1) | 90 | `CpuSetup` @ `0x0e3` (4) |
| Advanced > CPU Information | Limit CPUID Maximum | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x2ad` (1) |
| Advanced > CPU Information > CPU SMM Enhancement | SMM Code Access Check | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSmm` @ `0x001` (1) |
