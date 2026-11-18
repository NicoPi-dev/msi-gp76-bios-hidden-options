# Advanced > Debug Settings

Category: **Hidden - MSI advanced menu** - 22 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > Debug Settings | Kernel Debug Serial Port | Legacy UART (0x0) \| SERIALIO UART2 (0x3) | 0 | `PchSetup` @ `0x008` (1) |
| Advanced > Debug Settings | Platform Debug Consent | Disabled (0x0) \| Enabled (DCI OOB+[DbC]) (0x1) \| Enabled (DCI OOB) (0x2) \| Enabled (USB2 DbC) (0x5) \| Enabled (USB3 DbC) (0x3) \| Enabl… | Disabled | `PchSetup` @ `0x6e0` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | USB3 Type-C UFP2DFP Kernel/Platform Debug Support | Disabled (0x0) \| Enabled (0x1) \| No Change (0x2) | No Change | `PchSetup` @ `0x00a` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | SLP_S0# Override | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x012` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | S0ix Override Settings | No Change (0x0) \| DCI OOB (0x1) \| USB2 DbC (0x2) \| Auto (0x3) | Auto | `PchSetup` @ `0x013` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | USB Overcurrent Override for DbC | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x00b` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | PCH Trace Hub Enable Mode | Disabled (0x0) \| Target Debugger (0x1) \| Host Debugger (0x2) | Disabled | `PchSetup` @ `0x6b7` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | PCH TH Mem Buffer Size 0 | None/OS (0x0) \| 1MB (0x1) \| 8MB (0x2) \| 64MB (0x3) \| 128MB (0x4) \| 256MB (0x5) \| 512MB (0x6) | 64MB | `PchSetup` @ `0x6b8` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | PCH TH Mem Buffer Size 1 | None/OS (0x0) \| 1MB (0x1) \| 8MB (0x2) \| 64MB (0x3) \| 128MB (0x4) \| 256MB (0x5) \| 512MB (0x6) | 64MB | `PchSetup` @ `0x6b9` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | CPU Run Control | Disabled (0x0) \| Enabled (0x1) \| No Change (0x2) | No Change | `CpuSetup` @ `0x0dd` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | CPU Run Control Lock | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x0de` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | Processor trace memory allocation | Disabled (0xff) \| 4KB (0x0) \| 8KB (0x1) \| 16KB (0x2) \| 32KB (0x3) \| 64KB (0x4) \| 128KB (0x5) \| 256KB (0x6) \| 512KB (0x7) \| 1MB (0x… | Disabled | `CpuSetup` @ `0x0fd` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | Processor trace | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x0fe` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | Processor Trace OutPut Scheme | Single Range Output (0x0) \| ToPA Output (0x1) | Single Range Output | `CpuSetup` @ `0x0fc` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | SMM Processor Trace | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSmm` @ `0x005` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | JTAG C10 Power Gate | Disabled (0x1) \| Enabled (0x0) | Enabled | `CpuSetup` @ `0x008` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | Three Strike Counter | Disabled (0x1) \| Enabled (0x0) | Enabled | `CpuSetup` @ `0x100` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | CrashLog Feature | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x4f6` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | CrashLog On All Reset | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x4f7` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | PMC Debug Message Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x6e1` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | CPU Wakeup Timer | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x208` (1) |
| Advanced > Debug Settings > Advanced Debug Settings | Delayed Authentication Mode | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetupStorage` @ `0x00a` (1) |
