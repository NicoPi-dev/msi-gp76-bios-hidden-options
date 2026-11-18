# Advanced > CPU Information

Category: **Hidden - MSI advanced menu** - 32 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > CPU Information | C6DRAM | Disabled (0x0) \| Enabled (0x1) | 1 | `CpuSetup` @ `0x0df` (1) |
| Advanced > CPU Information | Software Guard Extensions (SGX) | Disabled (0x0) \| Enabled (0x1) \| Software Controlled (0x2) | Software Controlled | `CpuSetup` @ `0x0e0` (1) |
| Advanced > CPU Information | Select Owner EPOCH input type | No Change in Owner EPOCHs (0x0) \| Change to New Random Owner EPOCHs (0x1) \| Manual User Defined Owner EPOCHs (0x2) | 0 | `CpuSetup` @ `0x0e1` (1) |
| Advanced > CPU Information | Software Guard Extensions Epoch 0 | 0 … 18446744073709551615 (step 1) | 6142344250440060711 | `CpuSetupSgxEpochData` @ `0x000` (8) |
| Advanced > CPU Information | Software Guard Extensions Epoch 1 | 0 … 18446744073709551615 (step 1) | 15521488688214965697 | `CpuSetupSgxEpochData` @ `0x008` (8) |
| Advanced > CPU Information | PRMRR Size | INVALID PRMRR (0x0) \| 32MB (0x2000000) \| 64MB (0x4000000) \| 128MB (0x8000000) \| 256MB (0x10000000) | INVALID PRMRR | `CpuSetup` @ `0x0e7` (4) |
| Advanced > CPU Information | CPU Flex Ratio Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x003` (1) |
| Advanced > CPU Information | CPU Flex Ratio Settings | 0 … 63 (step 0) | 20 | `CpuSetup` @ `0x001` (1) |
| Advanced > CPU Information | Hardware Prefetcher | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x0ba` (1) |
| Advanced > CPU Information | Adjacent Cache Line Prefetch | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x0bb` (1) |
| Advanced > CPU Information | Intel Virtualization Technology | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x0b4` (1) |
| Advanced > CPU Information | PECI | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x004` (1) |
| Advanced > CPU Information | Active Processor Cores | All (0x0) \| 1 (0x1) \| 2 (0x2) \| 3 (0x3) \| 4 (0x4) \| 5 (0x5) \| 6 (0x6) \| 7 (0x7) \| 8 (0x8) \| 9 (0x9) | All | `CpuSetup` @ `0x006` (1) |
| Advanced > CPU Information | Hyper-Threading | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x005` (1) |
| Advanced > CPU Information | BIST | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x007` (1) |
| Advanced > CPU Information | AP threads Idle Manner | HALT Loop (0x1) \| MWAIT Loop (0x2) \| RUN Loop (0x3) | MWAIT Loop | `CpuSetup` @ `0x0fb` (1) |
| Advanced > CPU Information | AES | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x0b5` (1) |
| Advanced > CPU Information | MachineCheck | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x0b6` (1) |
| Advanced > CPU Information | MonitorMWait | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x0b7` (1) |
| Advanced > CPU Information | Intel Trusted Execution Technology | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x0bc` (1) |
| Advanced > CPU Information | Alias Check Request | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x0bf` (1) |
| Advanced > CPU Information | DPR Memory Size (MB) | 0 … 255 (step 1) | 4 | `CpuSetup` @ `0x0b8` (2) |
| Advanced > CPU Information | Reset AUX Content | yes (0x1) \| no (0x0) | no | `CpuSetup` @ `0x0be` (1) |
| Advanced > CPU Information | FCLK Frequency for Early Power On | Normal (800Mhz) (0x0) \| 1GHz (0x1) \| 400MHz (0x2) \| Auto (0x3) | Auto | `CpuSetup` @ `0x101` (1) |
| Advanced > CPU Information | Voltage Optimization | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `CpuSetup` @ `0x1db` (1) |
| Advanced > CPU Information > BIOS Guard | BIOS Guard | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x0db` (1) |
| Advanced > CPU Information > BIOS Guard | Enable Tools Interface | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x0dc` (1) |
| Advanced > CPU Information > CPU SMM Enhancement | SMM MSR Save State Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSmm` @ `0x000` (1) |
| Advanced > CPU Information > CPU SMM Enhancement | SMM Use Delay Indication | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSmm` @ `0x002` (1) |
| Advanced > CPU Information > CPU SMM Enhancement | SMM Use Block Indication | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSmm` @ `0x003` (1) |
| Advanced > CPU Information > CPU SMM Enhancement | SMM Use SMM en-US Indication | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSmm` @ `0x004` (1) |
| Advanced > CPU Information > CPU SMM Enhancement | DGR+NR11 / NR10 Support | NR10 (0x0) \| DGR_NR11 (0x1) | DGR_NR11 | `CpuSmm` @ `0x006` (1) |
