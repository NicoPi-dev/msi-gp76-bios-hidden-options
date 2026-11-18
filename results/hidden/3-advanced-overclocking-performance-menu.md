# Advanced > OverClocking Performance Menu

Category: **Hidden - MSI advanced menu** - 127 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > OverClocking Performance Menu | OverClocking Feature | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x1b7` (1) |
| Advanced > OverClocking Performance Menu | Per-core HT Disable | 0 … 511 (step 1) | 0 | `CpuSetup` @ `0x24b` (2) |
| Advanced > OverClocking Performance Menu | Automatic Easy Overclock | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x2ac` (1) |
| Advanced > OverClocking Performance Menu | WDT Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x020` (1) |
| Advanced > OverClocking Performance Menu | XTU Interface | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x1b8` (1) |
| Advanced > OverClocking Performance Menu | BCLK Aware Adaptive Voltage | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x207` (1) |
| Advanced > OverClocking Performance Menu > GT | GT OverClocking Frequency | 0 … 255 (step 1) | 0 | `SaSetup` @ `0x1e0` (1) |
| Advanced > OverClocking Performance Menu > GT | GT Voltage Mode | Adaptive (0x0) \| Override (0x1) | Adaptive | `SaSetup` @ `0x1e1` (1) |
| Advanced > OverClocking Performance Menu > GT | GT Voltage Override | 0 … 2000 (step 1) | 0 | `SaSetup` @ `0x1e5` (2) |
| Advanced > OverClocking Performance Menu > GT | GT Extra Turbo Voltage | 0 … 2000 (step 1) | 0 | `SaSetup` @ `0x1e7` (2) |
| Advanced > OverClocking Performance Menu > GT | GT Voltage Offset | 0 … 1000 (step 1) | 0 | `SaSetup` @ `0x1e2` (2) |
| Advanced > OverClocking Performance Menu > GT | Offset Prefix | + (0x0) \| - (0x1) | + | `SaSetup` @ `0x1e4` (1) |
| Advanced > OverClocking Performance Menu > GT | GT OverClocking Frequency | 0 … 60 (step 1) | 0 | `SaSetup` @ `0x1e9` (1) |
| Advanced > OverClocking Performance Menu > GT | GT Voltage Mode | Adaptive (0x0) \| Override (0x1) | Adaptive | `SaSetup` @ `0x1ea` (1) |
| Advanced > OverClocking Performance Menu > GT | GT Voltage Override | 0 … 2000 (step 1) | 0 | `SaSetup` @ `0x1ee` (2) |
| Advanced > OverClocking Performance Menu > GT | GT Extra Turbo Voltage | 0 … 2000 (step 1) | 0 | `SaSetup` @ `0x1f0` (2) |
| Advanced > OverClocking Performance Menu > GT | GTU Voltage Offset | 0 … 1000 (step 1) | 0 | `SaSetup` @ `0x1eb` (2) |
| Advanced > OverClocking Performance Menu > GT | Offset Prefix | + (0x0) \| - (0x1) | + | `SaSetup` @ `0x1ed` (1) |
| Advanced > OverClocking Performance Menu > Memory | Realtime Memory Timing | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x204` (1) |
| Advanced > OverClocking Performance Menu > Memory | Memory profile | Default profile (0x0) \| Custom profile (0x1) \| XMP profile 1 (0x2) \| XMP profile 2 (0x3) | Default profile | `SaSetup` @ `0x134` (1) |
| Advanced > OverClocking Performance Menu > Memory | Memory Reference Clock | 133 (0x0) \| 100 (0x1) | 133 | `SaSetup` @ `0x00c` (1) |
| Advanced > OverClocking Performance Menu > Memory | Memory Ratio | Auto (0x0) \| 3 (0x3) \| 4 (0x4) \| 5 (0x5) \| 6 (0x6) \| 7 (0x7) \| 8 (0x8) \| 9 (0x9) \| 10 (0xa) \| 11 (0xb) \| 12 (0xc) \| 13 (0xd) \| … | Auto | `SaSetup` @ `0x00e` (1) |
| Advanced > OverClocking Performance Menu > Memory | QCLK Odd Ratio | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x00f` (1) |
| Advanced > OverClocking Performance Menu > Memory | tCL | 0 … 36 (step 1) | 0 | `SaSetup` @ `0x010` (1) |
| Advanced > OverClocking Performance Menu > Memory | tRCD/tRP | 0 … 63 (step 1) | 0 | `SaSetup` @ `0x016` (1) |
| Advanced > OverClocking Performance Menu > Memory | tRAS | 0 … 90 (step 1) | 0 | `SaSetup` @ `0x014` (2) |
| Advanced > OverClocking Performance Menu > Memory | tCWL | 0 … 34 (step 1) | 0 | `SaSetup` @ `0x011` (1) |
| Advanced > OverClocking Performance Menu > Memory | tFAW | 0 … 127 (step 1) | 0 | `SaSetup` @ `0x012` (2) |
| Advanced > OverClocking Performance Menu > Memory | tREFI | 0 … 65535 (step 1) | 0 | `SaSetup` @ `0x017` (2) |
| Advanced > OverClocking Performance Menu > Memory | tRFC | 0 … 1023 (step 1) | 0 | `SaSetup` @ `0x019` (2) |
| Advanced > OverClocking Performance Menu > Memory | tRRD | 0 … 31 (step 1) | 0 | `SaSetup` @ `0x01b` (1) |
| Advanced > OverClocking Performance Menu > Memory | tRRD_L | 0 … 31 (step 1) | 0 | `SaSetup` @ `0x01c` (1) |
| Advanced > OverClocking Performance Menu > Memory | tRRD_S | 0 … 31 (step 1) | 0 | `SaSetup` @ `0x01d` (1) |
| Advanced > OverClocking Performance Menu > Memory | tRTP | 0 … 16 (step 1) | 0 | `SaSetup` @ `0x01e` (1) |
| Advanced > OverClocking Performance Menu > Memory | tWR | Auto (0x0) \| 5 (0x5) \| 6 (0x6) \| 7 (0x7) \| 8 (0x8) \| 10 (0xa) \| 12 (0xc) \| 14 (0xe) \| 16 (0x10) \| 18 (0x12) \| 20 (0x14) \| 22 (0x… | Auto | `SaSetup` @ `0x01f` (1) |
| Advanced > OverClocking Performance Menu > Memory | tWTR | 0 … 28 (step 1) | 0 | `SaSetup` @ `0x020` (1) |
| Advanced > OverClocking Performance Menu > Memory | tWTR_L | 0 … 60 (step 1) | 0 | `SaSetup` @ `0x021` (1) |
| Advanced > OverClocking Performance Menu > Memory | tWTR_S | 0 … 28 (step 1) | 0 | `SaSetup` @ `0x022` (1) |
| Advanced > OverClocking Performance Menu > Memory | Memory Voltage | Default (0x0) \| 0.60 Volts (0x258) \| 1.10 Volts (0x44c) \| 1.20 Volts (0x4b0) \| 1.25 Volts (0x4e2) \| 1.30 Volts (0x514) \| 1.35 Volts (… | Default | `SaSetup` @ `0x003` (2) |
| Advanced > OverClocking Performance Menu > Memory | NMode | 0 … 2 (step 1) | 0 | `SaSetup` @ `0x023` (1) |
| Advanced > OverClocking Performance Menu > Memory | Command Rate Support | Disabled (0x0) \| 1 CMD (0x1) \| 2 CMDs (0x2) \| 3 CMDs (0x3) \| 4 CMDs (0x4) \| 5 CMDs (0x5) \| 6 CMDs (0x6) \| 7 CMDs (0x7) | 3 CMDs | `SaSetup` @ `0x212` (1) |
| Advanced > OverClocking Performance Menu > Memory | DllBwEn[0] | 0 … 7 (step 1) | 0 | `SaSetup` @ `0x007` (1) |
| Advanced > OverClocking Performance Menu > Memory | DllBwEn[1] | 0 … 7 (step 1) | 1 | `SaSetup` @ `0x008` (1) |
| Advanced > OverClocking Performance Menu > Memory | DllBwEn[2] | 0 … 7 (step 1) | 2 | `SaSetup` @ `0x009` (1) |
| Advanced > OverClocking Performance Menu > Memory | DllBwEn[3] | 0 … 7 (step 1) | 2 | `SaSetup` @ `0x00a` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tRd2RdSG | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x170` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tRd2RdDG | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x171` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tRd2RdDR | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x172` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tRd2RdDD | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x173` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tRd2WrSG | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x17c` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tRd2WrDG | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x17d` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tRd2WrDR | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x17e` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tRd2WrDD | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x17f` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tWr2RdSG | 0 … 86 (step 1) | 0 | `SaSetup` @ `0x174` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tWr2RdDG | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x175` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tWr2RdDR | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x176` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tWr2RdDD | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x177` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tWr2WrSG | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x178` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tWr2WrDG | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x179` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tWr2WrDR | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x17a` (1) |
| Advanced > OverClocking Performance Menu > Memory > Turn Around Timing | tWr2WrDD | 0 … 54 (step 1) | 0 | `SaSetup` @ `0x17b` (1) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | VccCore Override Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x218` (1) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | VccCore | 800 … 2550 (step 10) | 1300 | `CpuSetup` @ `0x219` (2) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | VccST Override Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x21b` (1) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | VccST | 250 … 1500 (step 10) | 1020 | `CpuSetup` @ `0x21c` (2) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | VccSA Override Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x21f` (1) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | VccSA | 250 … 1520 (step 10) | 1050 | `CpuSetup` @ `0x220` (2) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | VccSFR_OC Override Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x222` (1) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | VccSFR_OC | 1000 … 2520 (step 10) | 1250 | `CpuSetup` @ `0x223` (2) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | VccSFR Override Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x226` (1) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | VccSFR | 690 … 2050 (step 10) | 1020 | `CpuSetup` @ `0x227` (2) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | VccIO Override Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x22a` (1) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | VccIO | 900 … 1520 (step 5) | 950 | `CpuSetup` @ `0x22b` (2) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | Core VR Loadline Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x233` (1) |
| Advanced > OverClocking Performance Menu > Platform Voltage Overrides | DC Loadline value | -100 uOhm (0x0) \| 0 uOhm (0x1) \| 100 uOhm (0x2) \| 700 uOhm (0x3) \| 900 uOhm (0x4) \| 1000 uOhm (0x5) \| 1200 uOhm (0x6) \| 1300 uOhm (0… | 2100 uOhm | `CpuSetup` @ `0x234` (1) |
| Advanced > OverClocking Performance Menu > Processor | Core Max OC Ratio | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x1b9` (1) |
| Advanced > OverClocking Performance Menu > Processor | Core Voltage Mode | Adaptive (0x0) \| Override (0x1) | Adaptive | `CpuSetup` @ `0x1ba` (1) |
| Advanced > OverClocking Performance Menu > Processor | Core Voltage Override | 0 … 2000 (step 1) | 0 | `CpuSetup` @ `0x1bb` (2) |
| Advanced > OverClocking Performance Menu > Processor | Core Extra Turbo Voltage | 0 … 2000 (step 1) | 0 | `CpuSetup` @ `0x1c0` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point Offset Mode | Legacy (0x0) \| Selection (0x1) | Legacy | `CpuSetup` @ `0x24e` (1) |
| Advanced > OverClocking Performance Menu > Processor | Core Voltage Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x1bd` (2) |
| Advanced > OverClocking Performance Menu > Processor | Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x1bf` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 1 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x250` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 1 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x26e` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 2 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x252` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 2 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x26f` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 3 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x254` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 3 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x270` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 4 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x256` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 4 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x271` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 5 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x258` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 5 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x272` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 6 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x25a` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 6 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x273` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 7 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x25c` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 7 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x274` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 8 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x25e` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 8 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x275` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 9 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x260` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 9 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x276` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 10 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x262` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 10 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x277` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 11 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x264` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 11 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x278` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 12 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x266` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 12 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x279` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 13 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x268` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 13 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x27a` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 14 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x26a` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 14 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x27b` (1) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 15 Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x26c` (2) |
| Advanced > OverClocking Performance Menu > Processor | VF Point 15 Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x27c` (1) |
| Advanced > OverClocking Performance Menu > Processor | AVX2 Ratio Offset | 0 … 31 (step 1) | 0 | `CpuSetup` @ `0x1c2` (1) |
| Advanced > OverClocking Performance Menu > Processor | TjMax Offset | 0 … 63 (step 1) | 0 | `CpuSetup` @ `0x1ec` (1) |
| Advanced > OverClocking Performance Menu > Processor | TVB Ratio Clipping | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x231` (1) |
| Advanced > OverClocking Performance Menu > Processor | TVB Voltage Optimizations | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x232` (1) |
| Advanced > OverClocking Performance Menu > Ring | Ring Max OC Ratio | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x1c4` (1) |
| Advanced > OverClocking Performance Menu > Ring | Ring Down Bin | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x1c5` (1) |
| Advanced > OverClocking Performance Menu > Ring | Min Ring Ratio Limit | 0 … 83 (step 1) | 0 | `CpuSetup` @ `0x20a` (1) |
| Advanced > OverClocking Performance Menu > Ring | Max Ring Ratio Limit | 0 … 83 (step 1) | 0 | `CpuSetup` @ `0x20c` (1) |
| Advanced > OverClocking Performance Menu > Uncore | Uncore Voltage Offset | 0 … 1000 (step 1) | 0 | `SaSetup` @ `0x1da` (2) |
| Advanced > OverClocking Performance Menu > Uncore | Offset Prefix | + (0x0) \| - (0x1) | + | `SaSetup` @ `0x1dc` (1) |
| Advanced > OverClocking Performance Menu > Voltage PLL Trim Controls | Core PLL Voltage Offset | 0 … 63 (step 1) | 0 | `CpuSetup` @ `0x1e7` (1) |
| Advanced > OverClocking Performance Menu > Voltage PLL Trim Controls | GT PLL Voltage Offset | 0 … 63 (step 1) | 0 | `CpuSetup` @ `0x1e8` (1) |
| Advanced > OverClocking Performance Menu > Voltage PLL Trim Controls | Ring PLL Voltage Offset | 0 … 63 (step 1) | 0 | `CpuSetup` @ `0x1e9` (1) |
| Advanced > OverClocking Performance Menu > Voltage PLL Trim Controls | System Agent PLL Voltage Offset | 0 … 63 (step 1) | 0 | `CpuSetup` @ `0x1ea` (1) |
| Advanced > OverClocking Performance Menu > Voltage PLL Trim Controls | Memory Controller PLL Voltage Offset | 0 … 63 (step 1) | 0 | `CpuSetup` @ `0x1eb` (1) |
