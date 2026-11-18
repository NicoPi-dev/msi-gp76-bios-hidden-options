# Advanced > Connectivity Configuration

Category: **Hidden - MSI advanced menu** - 99 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > Connectivity Configuration | CNVi Mode | Disable Integrated (0x0) \| Auto Detection (0x1) | Auto Detection | `PchSetup` @ `0x6d7` (1) |
| Advanced > Connectivity Configuration | BT Core | Enabled (0x1) \| Disabled (0x0) | Enabled | `PchSetup` @ `0x6d8` (1) |
| Advanced > Connectivity Configuration | BT Audio Offload | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x6d9` (1) |
| Advanced > Connectivity Configuration | CoExistence Manager | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x499` (1) |
| Advanced > Connectivity Configuration | Discrete Bluetooth Module | Disabled (0x0) \| Thunder Peak (0x1) | Disabled | `Setup` @ `0x2cc` (1) |
| Advanced > Connectivity Configuration | BT Interrupt Mode | GPIO Interrupt (0x0) \| APIC Interrupt (0x1) | GPIO Interrupt | `Setup` @ `0x2cd` (1) |
| Advanced > Connectivity Configuration | Advanced settings | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x443` (1) |
| Advanced > Connectivity Configuration | Switched Antenna Diversity Selection | Antenna1 (0x0) \| Antenna2 (0x1) \| Diversity (0x2) \| Diversity Antenna1 (0x3) \| Diversity Antenna2 (0x4) | Diversity | `Setup` @ `0x51b` (1) |
| Advanced > Connectivity Configuration | Domain Type SPLC 1 | 0 … 20 (step 1) | 7 | `Setup` @ `0x444` (1) |
| Advanced > Connectivity Configuration | Default Power Limit | 1 … 65535 (step 1) | 65535 | `Setup` @ `0x445` (2) |
| Advanced > Connectivity Configuration | Default Time Window | 1 … 100000 (step 1) | 30000 | `Setup` @ `0x447` (4) |
| Advanced > Connectivity Configuration | TRxDelay_A | 1 … 100 (step 1) | 50 | `Setup` @ `0x44b` (1) |
| Advanced > Connectivity Configuration | TRxCableLength_A | 1 … 100 (step 1) | 50 | `Setup` @ `0x44c` (1) |
| Advanced > Connectivity Configuration | TRxDelay_B | 1 … 100 (step 1) | 50 | `Setup` @ `0x44d` (1) |
| Advanced > Connectivity Configuration | TRxCableLength_B | 1 … 100 (step 1) | 50 | `Setup` @ `0x44e` (1) |
| Advanced > Connectivity Configuration | Domain Type | 0 … 100 (step 1) | 7 | `Setup` @ `0x44f` (1) |
| Advanced > Connectivity Configuration | Country Identifier | 1 … 65535 (step 1) | 16720 | `Setup` @ `0x450` (2) |
| Advanced > Connectivity Configuration | WiFi SAR | Disabled (0x0) \| Enabled (0x1) | 0 | `Setup` @ `0x455` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Set1 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x456` (1) |
| Advanced > Connectivity Configuration | SAR 5150-5350 MHz Set1 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x457` (1) |
| Advanced > Connectivity Configuration | SAR 5350-5470 MHz Set1 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x458` (1) |
| Advanced > Connectivity Configuration | SAR 5470-5725 MHz Set1 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x459` (1) |
| Advanced > Connectivity Configuration | SAR 5725-5950 MHz Set1 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x45a` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Set1 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x45b` (1) |
| Advanced > Connectivity Configuration | SAR 5150-5350 MHz Set1 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x45c` (1) |
| Advanced > Connectivity Configuration | SAR 5350-5470 MHz Set1 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x45d` (1) |
| Advanced > Connectivity Configuration | SAR 5470-5725 MHz Set1 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x45e` (1) |
| Advanced > Connectivity Configuration | SAR 5725-5950 MHz Set1 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x45f` (1) |
| Advanced > Connectivity Configuration | WiFi Dynamic SAR | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x460` (1) |
| Advanced > Connectivity Configuration | Extended SAR Range Sets | No Additional sets (0x0) \| Set 2 (0x1) \| Set 3 (0x2) \| Set 4 (0x3) | No Additional sets | `Setup` @ `0x461` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Set2 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x462` (1) |
| Advanced > Connectivity Configuration | SAR 5150-5350 MHz Set2 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x463` (1) |
| Advanced > Connectivity Configuration | SAR 5350-5470 MHz Set2 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x464` (1) |
| Advanced > Connectivity Configuration | SAR 5470-5725 MHz Set2 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x465` (1) |
| Advanced > Connectivity Configuration | SAR 5725-5950 MHz Set2 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x466` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Set2 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x467` (1) |
| Advanced > Connectivity Configuration | SAR 5150-5350 MHz Set2 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x468` (1) |
| Advanced > Connectivity Configuration | SAR 5350-5470 MHz Set2 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x469` (1) |
| Advanced > Connectivity Configuration | SAR 5470-5725 MHz Set2 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x46a` (1) |
| Advanced > Connectivity Configuration | SAR 5725-5950 MHz Set2 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x46b` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Set3 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x46c` (1) |
| Advanced > Connectivity Configuration | SAR 5150-5350 MHz Set3 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x46d` (1) |
| Advanced > Connectivity Configuration | SAR 5350-5470 MHz Set3 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x46e` (1) |
| Advanced > Connectivity Configuration | SAR 5470-5725 MHz Set3 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x46f` (1) |
| Advanced > Connectivity Configuration | SAR 5725-5950 MHz Set3 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x470` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Set3 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x471` (1) |
| Advanced > Connectivity Configuration | SAR 5150-5350 MHz Set3 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x472` (1) |
| Advanced > Connectivity Configuration | SAR 5350-5470 MHz Set3 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x473` (1) |
| Advanced > Connectivity Configuration | SAR 5470-5725 MHz Set3 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x474` (1) |
| Advanced > Connectivity Configuration | SAR 5725-5950 MHz Set3 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x475` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Set4 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x476` (1) |
| Advanced > Connectivity Configuration | SAR 5150-5350 MHz Set4 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x477` (1) |
| Advanced > Connectivity Configuration | SAR 5350-5470 MHz Set4 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x478` (1) |
| Advanced > Connectivity Configuration | SAR 5470-5725 MHz Set4 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x479` (1) |
| Advanced > Connectivity Configuration | SAR 5725-5950 MHz Set4 Chain A | 0 … 255 (step 1) | 0 | `Setup` @ `0x47a` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Set4 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x47b` (1) |
| Advanced > Connectivity Configuration | SAR 5150-5350 MHz Set4 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x47c` (1) |
| Advanced > Connectivity Configuration | SAR 5350-5470 MHz Set4 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x47d` (1) |
| Advanced > Connectivity Configuration | SAR 5470-5725 MHz Set4 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x47e` (1) |
| Advanced > Connectivity Configuration | SAR 5725-5950 MHz Set4 Chain B | 0 … 255 (step 1) | 0 | `Setup` @ `0x47f` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Max Allowed for Group 1 (FCC) | 0 … 255 (step 1) | 255 | `Setup` @ `0x480` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Chain A Offset for Group 1 (FCC) | 0 … 255 (step 1) | 0 | `Setup` @ `0x481` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Chain B Offset for Group 1 (FCC) | 0 … 255 (step 1) | 0 | `Setup` @ `0x482` (1) |
| Advanced > Connectivity Configuration | SAR 5200 MHz Max Allowed for Group 1 (FCC) | 0 … 255 (step 1) | 255 | `Setup` @ `0x483` (1) |
| Advanced > Connectivity Configuration | SAR 5200 MHz Chain A Offset for Group 1 (FCC) | 0 … 255 (step 1) | 0 | `Setup` @ `0x484` (1) |
| Advanced > Connectivity Configuration | SAR 5200 MHz Chain B Offset for Group 1 (FCC) | 0 … 255 (step 1) | 0 | `Setup` @ `0x485` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Max Allowed for Group 2 (EU Japan) | 0 … 255 (step 1) | 255 | `Setup` @ `0x486` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Chain A Offset for Group 2 (EU Japan) | 0 … 255 (step 1) | 0 | `Setup` @ `0x487` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Chain B Offset for Group 2 (EU Japan) | 0 … 255 (step 1) | 0 | `Setup` @ `0x488` (1) |
| Advanced > Connectivity Configuration | SAR 5200 MHz Max Allowed for Group 2 (EU Japan) | 0 … 255 (step 1) | 255 | `Setup` @ `0x489` (1) |
| Advanced > Connectivity Configuration | SAR 5200 MHz Chain A Offset for Group 2 (EU Japan) | 0 … 255 (step 1) | 0 | `Setup` @ `0x48a` (1) |
| Advanced > Connectivity Configuration | SAR 5200 MHz Chain B Offset for Group 2 (EU Japan) | 0 … 255 (step 1) | 0 | `Setup` @ `0x48b` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Max Allowed for Group 3 (ROW) | 0 … 255 (step 1) | 255 | `Setup` @ `0x48c` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Chain A Offset for Group 3 (ROW) | 0 … 255 (step 1) | 0 | `Setup` @ `0x48d` (1) |
| Advanced > Connectivity Configuration | SAR 2400 MHz Chain B Offset for Group 3 (ROW) | 0 … 255 (step 1) | 0 | `Setup` @ `0x48e` (1) |
| Advanced > Connectivity Configuration | SAR 5200 MHz Max Allowed for Group 3 (ROW) | 0 … 255 (step 1) | 255 | `Setup` @ `0x48f` (1) |
| Advanced > Connectivity Configuration | SAR 5200 MHz Chain A Offset for Group 3 (ROW) | 0 … 255 (step 1) | 0 | `Setup` @ `0x490` (1) |
| Advanced > Connectivity Configuration | SAR 5200 MHz Chain B Offset for Group 3 (ROW) | 0 … 255 (step 1) | 0 | `Setup` @ `0x491` (1) |
| Advanced > Connectivity Configuration | Wifi ANT Gain control | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x660` (1) |
| Advanced > Connectivity Configuration | ANT Gain 2400MHz Chain A | 0 … 255 (step 1) | 24 | `Setup` @ `0x661` (1) |
| Advanced > Connectivity Configuration | ANT Gain 5150MHz-5350MHz Chain A | 0 … 255 (step 1) | 40 | `Setup` @ `0x662` (1) |
| Advanced > Connectivity Configuration | Ant Gain 5350MHz-5470MHz Chain A | 0 … 255 (step 1) | 40 | `Setup` @ `0x663` (1) |
| Advanced > Connectivity Configuration | Ant Gain 5470MHz-5725MHz Chain A | 0 … 255 (step 1) | 40 | `Setup` @ `0x664` (1) |
| Advanced > Connectivity Configuration | Ant Gain 5725MHZ-5950MHz Chain A | 0 … 255 (step 1) | 40 | `Setup` @ `0x665` (1) |
| Advanced > Connectivity Configuration | Ant Gain 2400MHz Chain B | 0 … 255 (step 1) | 24 | `Setup` @ `0x666` (1) |
| Advanced > Connectivity Configuration | Ant Gain 5150MHz-5350MHz Chain B | 0 … 255 (step 1) | 40 | `Setup` @ `0x667` (1) |
| Advanced > Connectivity Configuration | Ant Gain 5350MHz-5470MHz Chain B | 0 … 255 (step 1) | 40 | `Setup` @ `0x668` (1) |
| Advanced > Connectivity Configuration | Ant Gain 5470MHz-5725MHz Chain B | 0 … 255 (step 1) | 40 | `Setup` @ `0x669` (1) |
| Advanced > Connectivity Configuration | Ant Gain 5725MHZ-5950MHz Chain B | 0 … 255 (step 1) | 40 | `Setup` @ `0x66a` (1) |
| Advanced > Connectivity Configuration | External 32kHz Clock | Not Valid (0x0) \| Valid (0x1) | Not Valid | `Setup` @ `0x66b` (1) |
| Advanced > Connectivity Configuration | Bluetooth SAR | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x494` (1) |
| Advanced > Connectivity Configuration | Bluetooth SAR BR | 0 … 255 (step 1) | 0 | `Setup` @ `0x495` (1) |
| Advanced > Connectivity Configuration | Bluetooth SAR EDR2 | 0 … 255 (step 1) | 0 | `Setup` @ `0x496` (1) |
| Advanced > Connectivity Configuration | Bluetooth SAR EDR3 | 0 … 255 (step 1) | 0 | `Setup` @ `0x497` (1) |
| Advanced > Connectivity Configuration | Bluetooth SAR LE | 0 … 255 (step 1) | 0 | `Setup` @ `0x498` (1) |
| Advanced > Connectivity Configuration | Bluetooth SAR LE 2Mhz | 0 … 255 (step 1) | 0 | `Setup` @ `0x51c` (1) |
| Advanced > Connectivity Configuration | Bluetooth SAR LE LR | 0 … 255 (step 1) | 0 | `Setup` @ `0x51d` (1) |
| Advanced > Connectivity Configuration > WWAN Configuration | WWAN Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x530` (1) |
| Advanced > Connectivity Configuration > WWAN Configuration | WWAN Reset Workaround | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x66c` (1) |
