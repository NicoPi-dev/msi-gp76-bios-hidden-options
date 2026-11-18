# Advanced > System Agent (SA) Configuration

Category: **Hidden - MSI advanced menu** - 369 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > System Agent (SA) Configuration | Stop Grant Configuration | Auto (0x1) \| Manual (0x0) | Auto | `SaSetup` @ `0x125` (1) |
| Advanced > System Agent (SA) Configuration | Number of Stop Grant Cycles | 1 … 63 (step 0) | 1 | `SaSetup` @ `0x126` (1) |
| Advanced > System Agent (SA) Configuration | VT-d | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x0f9` (1) |
| Advanced > System Agent (SA) Configuration | Control Iommu Pre-boot Behavior | Disable IOMMU (0x0) \| Enable IOMMU during boot without exception list (0x1) | 1 | `Setup` @ `0x536` (1) |
| Advanced > System Agent (SA) Configuration | CHAP Device (B0:D7:F0) | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x0f7` (1) |
| Advanced > System Agent (SA) Configuration | Thermal Device (B0:D4:F0) | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x0f8` (1) |
| Advanced > System Agent (SA) Configuration | GNA Device (B0:D8:F0) | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x0fb` (1) |
| Advanced > System Agent (SA) Configuration | CRID Support | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x1d2` (1) |
| Advanced > System Agent (SA) Configuration | Above 4GB MMIO BIOS assignment | Enabled (0x1) \| Disabled (0x0) | Enabled | `SaSetup` @ `0x0fa` (1) |
| Advanced > System Agent (SA) Configuration | X2APIC Opt Out | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x100` (1) |
| Advanced > System Agent (SA) Configuration | IPU Device (B0:D5:F0) | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x0fc` (1) |
| Advanced > System Agent (SA) Configuration | IPU IMR Configuration | IPU Camera (0x0) \| IPU Gen (0x1) | IPU Camera | `SaSetup` @ `0x0fd` (1) |
| Advanced > System Agent (SA) Configuration | eDRAM Mode | SW Mode eDRAM Off (0x0) \| SW Mode eDRAM On (0x1) \| eDRAM HW Mode (0x2) | eDRAM HW Mode | `SaSetup` @ `0x0fe` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration | DMI Max Link Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `SaSetup` @ `0x101` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration | DMI Gen3 Eq Phase 2 | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `SaSetup` @ `0x104` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration | DMI Gen3 Eq Phase 3 Method | Auto (0x0) \| Adaptive Hardware Equalization (0x1) \| Adaptive Software Equalization (0x2) \| Static Equalization (0x3) \| Disabled (0x4) | Auto | `SaSetup` @ `0x105` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration | Program Static Phase1 Eq | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x106` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration | DMI Link ASPM Control | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) | L1 | `SaSetup` @ `0x123` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration | DMI Extended Sync Control | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x124` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration | DMI De-emphasis Control | -6 dB (0x0) \| -3.5 dB (0x1) | -3.5 dB | `SaSetup` @ `0x103` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration | DMI IOT | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x102` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 Endpoint Hint value for each Lane | Lane 0 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x117` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 Endpoint Hint value for each Lane | Lane 1 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x118` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 Endpoint Hint value for each Lane | Lane 2 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x119` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 Endpoint Hint value for each Lane | Lane 3 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x11a` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 Endpoint Preset value for each Lane | Lane 0 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x10f` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 Endpoint Preset value for each Lane | Lane 1 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x110` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 Endpoint Preset value for each Lane | Lane 2 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x111` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 Endpoint Preset value for each Lane | Lane 3 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x112` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 Root Port Preset value for each Lane | Lane 0 | 0 … 9 (step 1) | 4 | `SaSetup` @ `0x107` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 Root Port Preset value for each Lane | Lane 1 | 0 … 9 (step 1) | 4 | `SaSetup` @ `0x108` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 Root Port Preset value for each Lane | Lane 2 | 0 … 9 (step 1) | 4 | `SaSetup` @ `0x109` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 Root Port Preset value for each Lane | Lane 3 | 0 … 9 (step 1) | 4 | `SaSetup` @ `0x10a` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 RxCTLE Control | Bundle0 | 0 … 15 (step 1) | 3 | `SaSetup` @ `0x11f` (1) |
| Advanced > System Agent (SA) Configuration > DMI/OPI Configuration > Gen3 RxCTLE Control | Bundle1 | 0 … 15 (step 1) | 3 | `SaSetup` @ `0x120` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | Graphics Turbo IMON Current | 14 … 31 (step 1) | 31 | `SaSetup` @ `0x12e` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | Skip Scaning of External Gfx Card | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x1d1` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | Primary Display | Auto (0x3) \| IGFX (0x0) \| PEG (0x1) \| PCI (0x2) \| SG (0x4) | 90 | `SaSetup` @ `0x127` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | Select PCIE Card | Auto (0x2) \| Elk Creek 4 (0x0) \| PEG Eval (0x1) | 90 | `SaSetup` @ `0x128` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | SG Delay After Power Enable | 0 … 1000 (step 0) | 300 | `SaSetup` @ `0x129` (2) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | SG Delay After Hold Reset | 0 … 1000 (step 0) | 100 | `SaSetup` @ `0x12b` (2) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | Internal Graphics | Auto (0x2) \| Disabled (0x0) \| Enabled (0x1) | 2 | `SaSetup` @ `0x12d` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | GTT Size | 2MB (0x1) \| 4MB (0x2) \| 8MB (0x3) | 8MB | `SaSetup` @ `0x043` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | Aperture Size | 128MB (0x0) \| 256MB (0x1) \| 512MB (0x3) \| 1024MB (0x7) \| 2048MB (0xf) | 256MB | `SaSetup` @ `0x044` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | PSMI SUPPORT | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x045` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | PSMI Region Size | 32MB (0x0) \| 288MB (0x1) \| 544MB (0x2) \| 800MB (0x3) \| 1024MB (0x4) | 90 | `SaSetup` @ `0x046` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | DVMT Pre-Allocated | 0M (0x0) \| 32M (0x1) \| 64M (0x2) \| 4M (0xf0) \| 8M (0xf1) \| 12M (0xf2) \| 16M (0xf3) \| 20M (0xf4) \| 24M (0xf5) \| 28M (0xf6) \| 32M/F… | 2 | `SaSetup` @ `0x0f5` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | DVMT Total Gfx Mem | 128M (0x1) \| 256M (0x2) \| MAX (0x3) | 2 | `SaSetup` @ `0x0f6` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | Intel Graphics Pei Display Peim | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x049` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | VDD Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x047` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | PM Support | Enabled (0x1) \| Disabled (0x0) | Enabled | `SaSetup` @ `0x048` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | PAVP Enable | Enabled (0x1) \| Disabled (0x0) | Enabled | `SaSetup` @ `0x04a` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | Cdynmax Clamping Enable | Enabled (0x1) \| Disabled (0x0) | Enabled | `SaSetup` @ `0x04c` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | Cd Clock Frequency | 337.5 Mhz (0x0) \| 450 Mhz (0x1) \| 540 Mhz (0x2) \| 675 Mhz (0x3) | 675 Mhz | `SaSetup` @ `0x04d` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | Skip CD Clock Init in S3 resume | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x20c` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration | IUER Button Enable | Disabled (0x0) \| Enabled (0x1) | 0 | `SaSetup` @ `0x1d7` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > Intel(R) Ultrabook Event Support | IUER Slate Enable | Disabled (0x0) \| Enabled (0x1) | 0 | `SaSetup` @ `0x1d8` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > Intel(R) Ultrabook Event Support | Slate Mode boot value | Slate Mode (0x0) \| Laptop Mode (0x1) | Laptop Mode | `SaSetup` @ `0x1d3` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > Intel(R) Ultrabook Event Support | Slate Mode on S3 and S4 resume | No change (0x0) \| Toggle (0x1) | No change | `SaSetup` @ `0x1d4` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > Intel(R) Ultrabook Event Support | IUER Dock Enable | Disabled (0x0) \| Enabled (0x1) | 0 | `SaSetup` @ `0x1d9` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > Intel(R) Ultrabook Event Support | Dock Mode boot value | Undocked (0x0) \| Docked (0x1) | Undocked | `SaSetup` @ `0x1d5` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > Intel(R) Ultrabook Event Support | Dock Mode upon S3 and S4 resume | No change (0x0) \| Toggle (0x1) | No change | `SaSetup` @ `0x1d6` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > LCD Control | Primary IGFX Boot Display | VBIOS Default (0x0) \| EFP (0x4) \| LFP (0x8) \| EFP3 (0x20) \| EFP2 (0x40) \| EFP4 (0x10) | VBIOS Default | `SaSetup` @ `0x03a` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > LCD Control | Secondary IGFX Boot Display | Disabled (0x0) \| EFP (0x4) \| EFP3 (0x20) \| EFP2 (0x40) \| EFP4 (0x10) | Disabled | `SaSetup` @ `0x03b` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > LCD Control | LCD Panel Type | VBIOS Default (0x0) \| 640x480    LVDS (0x1) \| 800x600    LVDS (0x2) \| 1024x768   LVDS (0x3) \| 1280x1024  LVDS (0x4) \| 1400x1050  LVDS1… | VBIOS Default | `SaSetup` @ `0x03c` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > LCD Control | Panel Scaling | Auto (0x0) \| Off (0x1) \| Force Scaling (0x6) | Auto | `SaSetup` @ `0x03d` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > LCD Control | Backlight Control | PWM Inverted (0x0) \| PWM Normal (0x2) | PWM Normal | `SaSetup` @ `0x03f` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > LCD Control | Active LFP | No eDP (0x0) \| eDP Port-A (0x3) | eDP Port-A | `SaSetup` @ `0x041` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > LCD Control | Panel Color Depth | 18 Bit (0x0) \| 24 Bit (0x1) | 18 Bit | `SaSetup` @ `0x042` (1) |
| Advanced > System Agent (SA) Configuration > Graphics Configuration > LCD Control | Backlight Brightness | 0 … 255 (step 0) | 255 | `SaSetup` @ `0x04b` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | MRC ULT Safe Config | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x1cb` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Safe Mode Support | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x142` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Memory Test on Warm Boot | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x211` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Maximum Memory Frequency | Auto (0x0) \| 1067 (0x42b) \| 1200 (0x4b0) \| 1333 (0x535) \| 1400 (0x578) \| 1600 (0x640) \| 1800 (0x708) \| 1867 (0x74b) \| 2000 (0x7d0) … | Auto | `SaSetup` @ `0x132` (2) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | HOB Buffer Size | Auto (0x0) \| 1B (0x1) \| 1KB (0x2) \| Max (assuming 63KB total HOB size) (0x3) | Auto | `SaSetup` @ `0x12f` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | ECC Support | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x130` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Max TOLUD | Dynamic (0x0) \| 1 GB (0x1) \| 1.25 GB (0x2) \| 1.5 GB (0x3) \| 1.75 GB (0x4) \| 2 GB (0x5) \| 2.25 GB (0x6) \| 2.5 GB (0x7) \| 2.75 GB (0x… | Dynamic | `SaSetup` @ `0x131` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | SA GV | Disabled (0x0) \| Fixed Low (0x1) \| Fixed High (0x2) \| Enabled (0x3) | Enabled | `SaSetup` @ `0x14a` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | SA GV Low Freq | MRC default (0x0) \| 1067 (0x42b) \| 1200 (0x4b0) \| 1333 (0x535) \| 1400 (0x578) \| 1600 (0x640) \| 1800 (0x708) \| 1867 (0x74b) \| 2133 (… | MRC default | `SaSetup` @ `0x14b` (2) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Retrain on Fast Fail | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x141` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | BER Support | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x145` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Enable RH Prevention | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x1cd` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Row Hammer Solution | Hardware RHP (0x0) \| 2x Refresh (0x1) | Hardware RHP | `SaSetup` @ `0x1ce` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | RH Activation Probability | 1/2^1 (0x1) \| 1/2^2 (0x2) \| 1/2^3 (0x3) \| 1/2^4 (0x4) \| 1/2^5 (0x5) \| 1/2^6 (0x6) \| 1/2^7 (0x7) \| 1/2^8 (0x8) \| 1/2^9 (0x9) \| 1/2^… | 1/2^11 | `SaSetup` @ `0x1cf` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Exit On Failure (MRC) | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x1d0` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Probeless Trace | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x146` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Memory Trace | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x147` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | GDXC IOT size | 0 … 128 (step 1) | 4 | `SaSetup` @ `0x148` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | GDXC MOT size | 0 … 128 (step 1) | 12 | `SaSetup` @ `0x149` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Enable/Disable IED (Intel Enhanced Debug) | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x0ff` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Ch Hash Support | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x139` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Ch Hash Mask | 0 … 16383 (step 1) | 0 | `SaSetup` @ `0x13a` (2) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Ch Hash Interleaved Bit | BIT6 (0x0) \| BIT7 (0x1) \| BIT8 (0x2) \| BIT9 (0x3) \| BIT10 (0x4) \| BIT11 (0x5) \| BIT12 (0x6) \| BIT13 (0x7) | BIT8 | `SaSetup` @ `0x13c` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Per Bank Refresh | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x13d` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Strong Weak Leaker | 1 … 7 (step 1) | 7 | `SaSetup` @ `0x13e` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Memory Scrambler | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x1c6` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Force ColdReset | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x1c7` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Channel A DIMM Control | Enable both DIMMs (0x0) \| Disable DIMM0 (0x1) \| Disable DIMM1 (0x2) \| Disable both DIMMs (0x3) | Enable both DIMMs | `SaSetup` @ `0x1c8` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Channel B DIMM Control | Enable both DIMMs (0x0) \| Disable DIMM0 (0x1) \| Disable DIMM1 (0x2) \| Disable both DIMMs (0x3) | Enable both DIMMs | `SaSetup` @ `0x1c9` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Force Single Rank | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x13f` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Memory Remap | Enabled (0x1) \| Disabled (0x0) | Enabled | `SaSetup` @ `0x1ca` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Time Measure | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x135` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | DLL Weak Lock Support | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x217` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Pwr Down Idle Timer | 0 … 255 (step 1) | 0 | `SaSetup` @ `0x216` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Fast Boot | Disabled (0x0) \| Enabled (0x1) | 1 | `SaSetup` @ `0x136` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Train On Warm boot | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x213` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Rank Margin Tool Per Task | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x137` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Training Tracing | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x138` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Lpddr Mem WL Set | Set A (0x0) \| Set B (0x1) | Set B | `SaSetup` @ `0x140` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | BDAT ACPI Table Support | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x001` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | BDAT Memory Test Type | Rank Margin Tool Rank (0x0) \| Rank Margin Tool Bit (0x1) \| Margin 2D (0x2) | Rank Margin Tool Rank | `SaSetup` @ `0x143` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Rank Margin Tool Loop Count | 0 … 32 (step 1) | 0 | `SaSetup` @ `0x144` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | Lpddr Dram Odt | Auto (0x2) \| Enabled (0x1) \| Disabled (0x0) | Auto | `SaSetup` @ `0x214` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration | DDR4 Skip Refresh Enable | Enabled (0x1) \| Disabled (0x0) | Enabled | `SaSetup` @ `0x215` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration | Memory Thermal Management | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x1c2` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration | PECI Injected Temperature | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x1c3` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration | EXTTS# via TS-on-Board | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x1c4` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration | EXTTS# via TS-on-DIMM | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x1c5` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling | DDR PowerDown and idle counter | PCODE (0x0) \| BIOS (0x1) | BIOS | `SaSetup` @ `0x183` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling | For LPDDR Only: DDR PowerDown and idle counter | PCODE (0x0) \| BIOS (0x1) | BIOS | `SaSetup` @ `0x184` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling | REFRESH_2X_MODE | Disabled (0x0) \| 1- Enabled for WARM or HOT (0x1) \| 2- Enabled HOT only (0x2) | Disabled | `SaSetup` @ `0x185` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling | LPDDR Thermal Sensor | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x186` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling | SelfRefresh Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x1bb` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling | SelfRefresh IdleTimer | 0 … 65535 (step 1) | 0 | `SaSetup` @ `0x1bc` (2) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling | Throttler CKEMin Defeature | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x1be` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling | Throttler CKEMin Timer | 0 … 255 (step 1) | 48 | `SaSetup` @ `0x1bf` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling | For LPDDR Only: Throttler CKEMin Defeature | Enabled (0x1) \| Disabled (0x0) | Enabled | `SaSetup` @ `0x1c0` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling | For LPDDR Only: Throttler CKEMin Timer | 0 … 255 (step 1) | 64 | `SaSetup` @ `0x1c1` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Use user provided power weights, scale factor, and channel power floor values | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x188` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Energy Scale Factor | 0 … 7 (step 1) | 4 | `SaSetup` @ `0x189` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Idle Energy Ch0Dimm0 | 0 … 63 (step 1) | 10 | `SaSetup` @ `0x1a8` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | PowerDown Energy Ch0Dimm0 | 0 … 63 (step 1) | 6 | `SaSetup` @ `0x1aa` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Activate Energy Ch0Dimm0 | 0 … 255 (step 1) | 172 | `SaSetup` @ `0x1ac` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Read Energy Ch0Dimm0 | 0 … 255 (step 1) | 212 | `SaSetup` @ `0x1ae` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Write Energy Ch0Dimm0 | 0 … 255 (step 1) | 221 | `SaSetup` @ `0x1b0` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Idle Energy Ch0Dimm1 | 0 … 63 (step 1) | 10 | `SaSetup` @ `0x1a7` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | PowerDown Energy Ch0Dimm1 | 0 … 63 (step 1) | 6 | `SaSetup` @ `0x1a9` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Activate Energy Ch0Dimm1 | 0 … 255 (step 1) | 172 | `SaSetup` @ `0x1ab` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Read Energy Ch0Dimm1 | 0 … 255 (step 1) | 212 | `SaSetup` @ `0x1ad` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Write Energy Ch0Dimm1 | 0 … 255 (step 1) | 221 | `SaSetup` @ `0x1af` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Idle Energy Ch1Dimm0 | 0 … 63 (step 1) | 10 | `SaSetup` @ `0x1b2` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | PowerDown Energy Ch1Dimm0 | 0 … 63 (step 1) | 6 | `SaSetup` @ `0x1b4` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Activate Energy Ch1Dimm0 | 0 … 255 (step 1) | 172 | `SaSetup` @ `0x1b6` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Read Energy Ch1Dimm0 | 0 … 255 (step 1) | 212 | `SaSetup` @ `0x1b8` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Write Energy Ch1Dimm0 | 0 … 255 (step 1) | 221 | `SaSetup` @ `0x1ba` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Idle Energy Ch1Dimm1 | 0 … 63 (step 1) | 10 | `SaSetup` @ `0x1b1` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | PowerDown Energy Ch1Dimm1 | 0 … 63 (step 1) | 6 | `SaSetup` @ `0x1b3` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Activate Energy Ch1Dimm1 | 0 … 255 (step 1) | 172 | `SaSetup` @ `0x1b5` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Read Energy Ch1Dimm1 | 0 … 255 (step 1) | 212 | `SaSetup` @ `0x1b7` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Dram Power Meter | Write Energy Ch1Dimm1 | 0 … 255 (step 1) | 221 | `SaSetup` @ `0x1b9` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory RAPL | Rapl Power Floor Ch0 | 0 … 255 (step 1) | 0 | `SaSetup` @ `0x18b` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory RAPL | Rapl Power Floor Ch1 | 0 … 255 (step 1) | 0 | `SaSetup` @ `0x18a` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory RAPL | RAPL PL Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x18c` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory RAPL | RAPL PL 1 enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x194` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory RAPL | RAPL PL 1 Power | 0 … 16383 (step 1) | 90 | `SaSetup` @ `0x195` (2) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory RAPL | RAPL PL 1 WindowX | 0 … 3 (step 1) | 90 | `SaSetup` @ `0x192` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory RAPL | RAPL PL 1 WindowY | 0 … 31 (step 1) | 90 | `SaSetup` @ `0x193` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory RAPL | RAPL PL 2 enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x18f` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory RAPL | RAPL PL 2 Power | 0 … 16383 (step 1) | 222 | `SaSetup` @ `0x190` (2) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory RAPL | RAPL PL 2 WindowX | 0 … 3 (step 1) | 1 | `SaSetup` @ `0x18d` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory RAPL | RAPL PL 2 WindowY | 0 … 31 (step 1) | 10 | `SaSetup` @ `0x18e` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Lock Thermal Management Registers | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x187` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Extern Therm Status | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x180` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Closed Loop Therm Manage | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x181` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Open Loop Therm Manage | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x182` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Warm Threshold Ch0 Dimm0 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x197` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Warm Threshold Ch0 Dimm1 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x198` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Hot Threshold Ch0 Dimm0 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x19b` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Hot Threshold Ch0 Dimm1 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x19c` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Warm Threshold Ch1 Dimm0 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x199` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Warm Threshold Ch1 Dimm1 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x19a` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Hot Threshold Ch1 Dimm0 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x19d` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Hot Threshold Ch1 Dimm1 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x19e` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Warm Budget Ch0 Dimm0 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x19f` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Warm Budget Ch0 Dimm1 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x1a0` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Hot Budget Ch0 Dimm0 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x1a3` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Hot Budget Ch0 Dimm1 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x1a4` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Warm Budget Ch1 Dimm0 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x1a1` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Warm Budget Ch1 Dimm1 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x1a2` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Hot Budget Ch1 Dimm0 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x1a5` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Thermal Configuration > Memory Power and Thermal Throttling > Memory Thermal Reporting | Hot Budget Ch1 Dimm1 | 0 … 255 (step 1) | 255 | `SaSetup` @ `0x1a6` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Early Command Training | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x150` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | SenseAmp Offset Training | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x151` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Early ReadMPR Timing Centering 2D | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x152` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Read MPR Training | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x153` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Receive Enable Training | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x154` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Jedec Write Leveling | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x155` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | LPDDR4 Write DQ DQS Retraining | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x1cc` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Early Write Time Centering 2D | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x156` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Early Read Time Centering 2D | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x157` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Write Timing Centering 1D | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x158` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Write Voltage Centering 1D | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x159` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Read Timing Centering 1D | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x15a` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Dimm ODT Training* | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x15b` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | DIMM RON Training* | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x15c` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Write Drive Strength/Equalization 2D* | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x15d` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Write Slew Rate Training* | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x15e` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Read ODT Training* | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x15f` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Read Equalization Training* | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x160` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Read Amplifier Training* | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x161` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Write Timing Centering 2D | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x162` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Read Timing Centering 2D | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x163` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Command Voltage Centering | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x166` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Write Voltage Centering 2D | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x164` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Read Voltage Centering 2D | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x165` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Late Command Training | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x167` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Round Trip Latency | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x168` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Turn Around Timing Training | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x169` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Rank Margin Tool | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x16a` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Margin Check Limit | Disabled (0x0) \| L1 (0x1) \| L2 (0x2) \| Both (0x3) | Disabled | `SaSetup` @ `0x14d` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Margin Limit Check L2 | 1 … 300 (step 1) | 100 | `SaSetup` @ `0x14e` (2) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Memory Test | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x16b` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | DIMM SPD Alias Test | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x16c` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Receive Enable Centering 1D | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x16d` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Retrain Margin Check | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x16e` (1) |
| Advanced > System Agent (SA) Configuration > Memory Configuration > Memory Training Algorithms | Write Drive Strength Up/Dn independently | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x16f` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Enable Root Port | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `SaSetup` @ `0x05d` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Max Link Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `SaSetup` @ `0x061` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Max Link Width | Auto (0x0) \| Force X1 (0x1) \| Force X2 (0x2) \| Force X4 (0x3) \| Force X8 (0x4) | Auto | `SaSetup` @ `0x065` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Power Down Unused Lanes | Disabled (0x0) \| Auto (0x1) | Auto | `SaSetup` @ `0x069` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Gen3 Eq Phase 2 | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `SaSetup` @ `0x075` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Gen3 Eq Phase 3 Method | Auto (0x0) \| Adaptive Hardware Equalization (0x1) \| Adaptive Software Equalization (0x2) \| Static Equalization (0x3) \| Disabled (0x4) | Auto | `SaSetup` @ `0x071` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | ASPM | Disabled (0x0) \| Auto (0x4) \| ASPM L0s (0x1) \| ASPM L1 (0x2) \| ASPM L0sL1 (0x3) | ASPM L1 | `SaSetup` @ `0x055` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | ASPM L0s | Root Port Only (0x1) \| Endpoint Port Only (0x2) \| Both Root and Endpoint Ports (0x3) | Both Root and Endpoint Ports | `SaSetup` @ `0x059` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | De-emphasis Control | -6 dB (0x0) \| -3.5 dB (0x1) | -3.5 dB | `SaSetup` @ `0x079` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | OBFF | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x085` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x081` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG0 Slot Power Limit Value | 0 … 255 (step 1) | 75 | `SaSetup` @ `0x0d8` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG0 Slot Power Limit Scale | 1.0x (0x0) \| 0.1x (0x1) \| 0.01x (0x2) \| 0.001x (0x3) | 1.0x | `SaSetup` @ `0x0d4` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG0 Physical Slot Number | 0 … 8191 (step 1) | 1 | `SaSetup` @ `0x0dc` (2) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG0 Hotplug | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x0d0` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `SaSetup` @ `0x0e4` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Reseved Memory | 1 … 20 (step 1) | 10 | `SaSetup` @ `0x0e7` (2) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Reserved I/O | 4 … 20 (step 4) | 4 | `SaSetup` @ `0x0ed` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Enable Root Port | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `SaSetup` @ `0x05e` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Max Link Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `SaSetup` @ `0x062` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Max Link Width | Auto (0x0) \| Force X1 (0x1) \| Force X2 (0x2) \| Force X4 (0x3) | Auto | `SaSetup` @ `0x066` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Power Down Unused Lanes | Disabled (0x0) \| Auto (0x1) | Auto | `SaSetup` @ `0x06a` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Gen3 Eq Phase 2 | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `SaSetup` @ `0x076` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Gen3 Eq Phase 3 Method | Auto (0x0) \| Adaptive Hardware Equalization (0x1) \| Adaptive Software Equalization (0x2) \| Static Equalization (0x3) \| Disabled (0x4) | Auto | `SaSetup` @ `0x072` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | ASPM | Disabled (0x0) \| Auto (0x4) \| ASPM L0s (0x1) \| ASPM L1 (0x2) \| ASPM L0sL1 (0x3) | Auto | `SaSetup` @ `0x056` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | ASPM L0s | Root Port Only (0x1) \| Endpoint Port Only (0x2) \| Both Root and Endpoint Ports (0x3) | Both Root and Endpoint Ports | `SaSetup` @ `0x05a` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | De-emphasis Control | -6 dB (0x0) \| -3.5 dB (0x1) | -3.5 dB | `SaSetup` @ `0x07a` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | OBFF | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x086` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x082` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG1 Slot Power Limit Value | 0 … 255 (step 1) | 75 | `SaSetup` @ `0x0d9` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG1 Slot Power Limit Scale | 1.0x (0x0) \| 0.1x (0x1) \| 0.01x (0x2) \| 0.001x (0x3) | 1.0x | `SaSetup` @ `0x0d5` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG1 Physical Slot Number | 0 … 8191 (step 1) | 2 | `SaSetup` @ `0x0de` (2) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG1 Hotplug | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x0d1` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `SaSetup` @ `0x0e5` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Reseved Memory | 1 … 20 (step 1) | 10 | `SaSetup` @ `0x0e9` (2) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Reserved I/O | 4 … 20 (step 4) | 4 | `SaSetup` @ `0x0ee` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Enable Root Port | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `SaSetup` @ `0x05f` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Max Link Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `SaSetup` @ `0x063` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Max Link Width | Auto (0x0) \| Force X1 (0x1) \| Force X2 (0x2) | Auto | `SaSetup` @ `0x067` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Power Down Unused Lanes | Disabled (0x0) \| Auto (0x1) | Auto | `SaSetup` @ `0x06b` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Gen3 Eq Phase 2 | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `SaSetup` @ `0x077` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Gen3 Eq Phase 3 Method | Auto (0x0) \| Adaptive Hardware Equalization (0x1) \| Adaptive Software Equalization (0x2) \| Static Equalization (0x3) \| Disabled (0x4) | Auto | `SaSetup` @ `0x073` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | ASPM | Disabled (0x0) \| Auto (0x4) \| ASPM L0s (0x1) \| ASPM L1 (0x2) \| ASPM L0sL1 (0x3) | Auto | `SaSetup` @ `0x057` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | ASPM L0s | Root Port Only (0x1) \| Endpoint Port Only (0x2) \| Both Root and Endpoint Ports (0x3) | Both Root and Endpoint Ports | `SaSetup` @ `0x05b` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | De-emphasis Control | -6 dB (0x0) \| -3.5 dB (0x1) | -3.5 dB | `SaSetup` @ `0x07b` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | OBFF | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x087` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x083` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG2 Slot Power Limit Value | 0 … 255 (step 1) | 75 | `SaSetup` @ `0x0da` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG2 Slot Power Limit Scale | 1.0x (0x0) \| 0.1x (0x1) \| 0.01x (0x2) \| 0.001x (0x3) | 1.0x | `SaSetup` @ `0x0d6` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG2 Physical Slot Number | 0 … 8191 (step 1) | 3 | `SaSetup` @ `0x0e0` (2) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG2 Hotplug | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x0d2` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `SaSetup` @ `0x0e6` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Reseved Memory | 1 … 20 (step 1) | 10 | `SaSetup` @ `0x0eb` (2) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Reserved I/O | 4 … 20 (step 4) | 4 | `SaSetup` @ `0x0ef` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Enable Root Port | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `SaSetup` @ `0x060` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Max Link Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `SaSetup` @ `0x064` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Max Link Width | Auto (0x0) \| Force X1 (0x1) \| Force X2 (0x2) | Auto | `SaSetup` @ `0x068` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Power Down Unused Lanes | Disabled (0x0) \| Auto (0x1) | Auto | `SaSetup` @ `0x06c` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Gen3 Eq Phase 2 | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `SaSetup` @ `0x078` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Gen3 Eq Phase 3 Method | Auto (0x0) \| Adaptive Hardware Equalization (0x1) \| Adaptive Software Equalization (0x2) \| Static Equalization (0x3) \| Disabled (0x4) | Auto | `SaSetup` @ `0x074` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | ASPM | Disabled (0x0) \| Auto (0x4) \| ASPM L0s (0x1) \| ASPM L1 (0x2) \| ASPM L0sL1 (0x3) | Auto | `SaSetup` @ `0x058` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | ASPM L0s | Root Port Only (0x1) \| Endpoint Port Only (0x2) \| Both Root and Endpoint Ports (0x3) | Both Root and Endpoint Ports | `SaSetup` @ `0x05c` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | De-emphasis Control | -6 dB (0x0) \| -3.5 dB (0x1) | -3.5 dB | `SaSetup` @ `0x07c` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | OBFF | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x088` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x084` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG3 Slot Power Limit Value | 0 … 255 (step 1) | 75 | `SaSetup` @ `0x0db` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG3 Slot Power Limit Scale | 1.0x (0x0) \| 0.1x (0x1) \| 0.01x (0x2) \| 0.001x (0x3) | 1.0x | `SaSetup` @ `0x0d7` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG3 Physical Slot Number | 0 … 8191 (step 1) | 3 | `SaSetup` @ `0x0e2` (2) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG2 Hotplug | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x0d3` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG0 Max Payload size | Auto (0xff) \| 128 (0x0) \| 256 TLP (0x1) | Auto | `SaSetup` @ `0x07d` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG1 Max Payload size | Auto (0xff) \| 128 (0x0) \| 256 TLP (0x1) | Auto | `SaSetup` @ `0x07e` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG2 Max Payload size | Auto (0xff) \| 128 (0x0) \| 256 TLP (0x1) | Auto | `SaSetup` @ `0x07f` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG3 Max Payload size | Auto (0xff) \| 128 (0x0) \| 256 TLP (0x1) | Auto | `SaSetup` @ `0x080` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Program PCIe ASPM after OpROM | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x0c5` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Program Static Phase1 Eq | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x089` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Always Attempt SW EQ | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x0c4` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Number of Presets to test | 7, 3, 5, 8 (0x0) \| 0 - 9 (0x1) \| Auto (0x2) | Auto | `SaSetup` @ `0x0cf` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Allow PERST# GPIO Usage | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x0c6` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | SW EQ Enable VOC | Jitter Only Test Mode (0x0) \| Jitter & VOC Test Mode (0x1) \| Auto (0x2) | Auto | `SaSetup` @ `0x0ca` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Jitter Dwell Time | 0 … 65535 (step 1) | 3000 | `SaSetup` @ `0x0c2` (2) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Jitter Error Target | 1 … 65535 (step 1) | 2 | `SaSetup` @ `0x0c7` (2) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | VOC Dwell Time | 0 … 65535 (step 1) | 10000 | `SaSetup` @ `0x0cb` (2) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | VOC Error Target | 1 … 65535 (step 1) | 2 | `SaSetup` @ `0x0cd` (2) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Generate BDAT PEG Margin Data | Disabled (0x0) \| Generate Port Jitter Data (0x1) | Disabled | `SaSetup` @ `0x0c9` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG IMR | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x20d` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG IMR Size | 0 … 1024 (step 1) | 0 | `SaSetup` @ `0x20e` (2) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | RP index for IMR | 1 … 4 (step 1) | 1 | `SaSetup` @ `0x210` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PCIe Rx CEM Test Mode | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x06d` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PEG Lane number for Test | 0 … 15 (step 1) | 0 | `SaSetup` @ `0x06e` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | Non-Protocol Awareness | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x06f` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration | PCIe Spread Spectrum Clocking | Enabled (0x0) \| Disabled (0x1) | Enabled | `SaSetup` @ `0x070` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 0 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0aa` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 1 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0ab` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 2 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0ac` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 3 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0ad` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 4 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0ae` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 5 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0af` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 6 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0b0` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 7 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0b1` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 8 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0b2` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 9 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0b3` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 10 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0b4` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 11 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0b5` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 12 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0b6` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 13 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0b7` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 14 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0b8` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Hint value for each Lane | Lane 15 | 0 … 6 (step 1) | 2 | `SaSetup` @ `0x0b9` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 0 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x09a` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 1 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x09b` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 2 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x09c` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 3 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x09d` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 4 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x09e` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 5 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x09f` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 6 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x0a0` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 7 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x0a1` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 8 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x0a2` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 9 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x0a3` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 10 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x0a4` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 11 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x0a5` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 12 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x0a6` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 13 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x0a7` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 14 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x0a8` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Endpoint Preset value for each Lane | Lane 15 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x0a9` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 0 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x08a` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 1 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x08b` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 2 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x08c` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 3 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x08d` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 4 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x08e` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 5 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x08f` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 6 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x090` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 7 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x091` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 8 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x092` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 9 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x093` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 10 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x094` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 11 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x095` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 12 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x096` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 13 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x097` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 14 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x098` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 Root Port Preset value for each Lane | Lane 15 | 0 … 9 (step 1) | 7 | `SaSetup` @ `0x099` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | Bundle0 | 0 … 15 (step 1) | 0 | `SaSetup` @ `0x0ba` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | Bundle1 | 0 … 15 (step 1) | 0 | `SaSetup` @ `0x0bb` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | Bundle2 | 0 … 15 (step 1) | 0 | `SaSetup` @ `0x0bc` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | Bundle3 | 0 … 15 (step 1) | 0 | `SaSetup` @ `0x0bd` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | Bundle4 | 0 … 15 (step 1) | 0 | `SaSetup` @ `0x0be` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | Bundle5 | 0 … 15 (step 1) | 0 | `SaSetup` @ `0x0bf` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | Bundle6 | 0 … 15 (step 1) | 0 | `SaSetup` @ `0x0c0` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | Bundle7 | 0 … 15 (step 1) | 0 | `SaSetup` @ `0x0c1` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | PEG10 RxCTLE Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x207` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | PEG11 RxCTLE Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x208` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | PEG12 RxCTLE Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x209` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | PEG60 RxCTLE Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x20a` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > Gen3 RxCTLE Control | DMI RxCTLE Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x20b` (1) |
| Advanced > System Agent (SA) Configuration > PEG Port Configuration > PEG Port Feature Configuration | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x737` (1) |
