# MSI GP76 Leopard (MS-17K2) BIOS E17K2IMS.30F - notable hidden options

A hand-picked subset (power limits, voltage offsets, locks, thermal, graphics, security).

| Category | Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|---|
| Hidden - MSI advanced menu | Advanced > CPU Information | Software Guard Extensions (SGX) | Disabled (0x0) \| Enabled (0x1) \| Software Controlled (0x2) | Software Controlled | `CpuSetup` @ `0x0e0` (1) |
| Hidden - MSI advanced menu | Advanced > CPU Information | Intel Virtualization Technology | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x0b4` (1) |
| Hidden - MSI advanced menu | Advanced > CPU Information | Hyper-Threading | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x005` (1) |
| Hidden - MSI advanced menu | Advanced > OverClocking Performance Menu > GT | GT Voltage Offset | 0 … 1000 (step 1) | 0 | `SaSetup` @ `0x1e2` (2) |
| Hidden - MSI advanced menu | Advanced > OverClocking Performance Menu > GT | Offset Prefix | + (0x0) \| - (0x1) | + | `SaSetup` @ `0x1e4` (1) |
| Hidden - MSI advanced menu | Advanced > OverClocking Performance Menu > Processor | Core Max OC Ratio | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x1b9` (1) |
| Hidden - MSI advanced menu | Advanced > OverClocking Performance Menu > Processor | Core Voltage Offset | 0 … 1000 (step 1) | 0 | `CpuSetup` @ `0x1bd` (2) |
| Hidden - MSI advanced menu | Advanced > OverClocking Performance Menu > Processor | Offset Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x1bf` (1) |
| Hidden - MSI advanced menu | Advanced > OverClocking Performance Menu > Ring | Ring Down Bin | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x1c5` (1) |
| Hidden - MSI advanced menu | Advanced > OverClocking Performance Menu > Uncore | Uncore Voltage Offset | 0 … 1000 (step 1) | 0 | `SaSetup` @ `0x1da` (2) |
| Hidden - MSI advanced menu | Advanced > OverClocking Performance Menu > Uncore | Offset Prefix | + (0x0) \| - (0x1) | + | `SaSetup` @ `0x1dc` (1) |
| Hidden - MSI advanced menu | Advanced > PCH-FW Configuration | ME State | Disabled (0x0) \| Enabled (0x1) | Enabled | `MeSetupStorage` @ `0x002` (1) |
| Hidden - MSI advanced menu | Advanced > PCH-IO Configuration | Flash Protection Range Registers (FPRR) | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x6dd` (1) |
| Hidden - MSI advanced menu | Advanced > PCH-IO Configuration > Security Configuration | BIOS Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x017` (1) |
| Hidden - MSI advanced menu | Advanced > Platform Settings | DGPU Power Enable | Enabled (0x1) \| Disabled (0x0) | Disabled | `Setup` @ `0x527` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control | Intel(R) SpeedStep(tm) | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x009` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control | Turbo Mode | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x011` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control | Power Limit 4 Override | Disabled (0x0) \| Enabled (0x1) | 0 | `CpuSetup` @ `0x025` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control | Power Limit 4 | 0 … 1023875 (step 125) | 0 | `CpuSetup` @ `0x026` (4) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control | Power Limit 4 Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x02a` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control | Enhanced C-states | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x010` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control | C-State Auto Demotion | Disabled (0x0) \| C1 (0x1) \| C3 (0x2) \| C1 and C3 (0x3) | C1 and C3 | `CpuSetup` @ `0x039` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control | Package C State Limit | C0/C1 (0x0) \| C2 (0x1) \| C3 (0x2) \| C6 (0x3) \| C7 (0x4) \| C7S (0x5) \| C8 (0x6) \| C9 (0x7) \| C10 (0x8) \| Cpu Default (0xfe) \| Auto… | 255 | `CpuSetup` @ `0x046` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control > CPU Lock Configuration | CFG Lock | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x03e` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control > CPU Lock Configuration | Overclocking Lock | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x0da` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Power Limit 1 | 0 … 4095875 (step 125) | 200000 | `CpuSetup` @ `0x056` (4) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Power Limit 2 | 0 … 4095875 (step 125) | 200000 | `CpuSetup` @ `0x05a` (4) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Power Limit 1 Time Window | 0 (0x0) \| 1 (0x1) \| 2 (0x2) \| 3 (0x3) \| 4 (0x4) \| 5 (0x5) \| 6 (0x6) \| 7 (0x7) \| 8 (0x8) \| 10 (0xa) \| 12 (0xc) \| 14 (0xe) \| 16 (… | 0 | `CpuSetup` @ `0x05e` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Power Limit 1 Override | Disabled (0x0) \| Enabled (0x1) | 0 | `CpuSetup` @ `0x016` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Power Limit 1 | 0 … 4095875 (step 125) | 0 | `CpuSetup` @ `0x012` (4) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Power Limit 1 Time Window | 0 (0x0) \| 1 (0x1) \| 2 (0x2) \| 3 (0x3) \| 4 (0x4) \| 5 (0x5) \| 6 (0x6) \| 7 (0x7) \| 8 (0x8) \| 10 (0xa) \| 12 (0xc) \| 14 (0xe) \| 16 (… | 0 | `CpuSetup` @ `0x017` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Power Limit 2 Override | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x018` (1) |
| Hidden - MSI advanced menu | Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Power Limit 2 | 0 … 4095875 (step 125) | 0 | `CpuSetup` @ `0x019` (4) |
| Hidden - MSI advanced menu | Advanced > System Agent (SA) Configuration | VT-d | Disabled (0x0) \| Enabled (0x1) | Enabled | `SaSetup` @ `0x0f9` (1) |
| Hidden - MSI advanced menu | Advanced > System Agent (SA) Configuration | Above 4GB MMIO BIOS assignment | Enabled (0x1) \| Disabled (0x0) | Enabled | `SaSetup` @ `0x0fa` (1) |
| Hidden - MSI advanced menu | Advanced > System Agent (SA) Configuration > Graphics Configuration | Primary Display | Auto (0x3) \| IGFX (0x0) \| PEG (0x1) \| PCI (0x2) \| SG (0x4) | 90 | `SaSetup` @ `0x127` (1) |
| Hidden - MSI advanced menu | Advanced > System Agent (SA) Configuration > Graphics Configuration | Internal Graphics | Auto (0x2) \| Disabled (0x0) \| Enabled (0x1) | 2 | `SaSetup` @ `0x12d` (1) |
| Hidden - MSI advanced menu | Advanced > System Agent (SA) Configuration > Graphics Configuration | Aperture Size | 128MB (0x0) \| 256MB (0x1) \| 512MB (0x3) \| 1024MB (0x7) \| 2048MB (0xf) | 256MB | `SaSetup` @ `0x044` (1) |
| Hidden - MSI advanced menu | Advanced > System Agent (SA) Configuration > Graphics Configuration | DVMT Pre-Allocated | 0M (0x0) \| 32M (0x1) \| 64M (0x2) \| 4M (0xf0) \| 8M (0xf1) \| 12M (0xf2) \| 16M (0xf3) \| 20M (0xf4) \| 24M (0xf5) \| 28M (0xf6) \| 32M/F… | 2 | `SaSetup` @ `0x0f5` (1) |
| Hidden - MSI advanced menu | Advanced > Thermal Configuration > CPU Thermal Configuration | Tcc Activation Offset | 0 … 63 (step 0) | 5 | `CpuSetup` @ `0x07a` (1) |
| Hidden - MSI advanced menu | Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Intel(R) Dynamic Tuning | Disabled (0x0) \| Enabled (0x1) | 1 | `Setup` @ `0x3a8` (1) |
| Hidden - MSI advanced menu | Advanced > Thermal Configuration > Platform Thermal Configuration | Critical Trip Point | 15 C (0xf) \| 23 C (0x17) \| 31 C (0x1f) \| 39 C (0x27) \| 47 C (0x2f) \| 55 C (0x37) \| 63 C (0x3f) \| 71 C (0x47) \| 79 C (0x4f) \| 87 C … | 119 | `Setup` @ `0x396` (1) |
| Hidden - MSI advanced menu | Advanced > Thermal Configuration > Platform Thermal Configuration | Critical Trip Points | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x39c` (1) |
| Hidden - MSI advanced menu | Advanced > Thermal Configuration > Platform Thermal Configuration | CPU Fan Speed | 1 … 100 (step 1) | 65 | `Setup` @ `0x3a7` (1) |
