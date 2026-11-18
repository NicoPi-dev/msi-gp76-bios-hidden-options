# Advanced > Thermal Configuration

Category: **Hidden - MSI advanced menu** - 145 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > Thermal Configuration > CPU Thermal Configuration | DTS SMM | Disabled (0x0) \| Enabled (0x1) \| Critical Temp Reporting (Out Of spec) (0x2) | Disabled | `CpuSetup` @ `0x1b6` (1) |
| Advanced > Thermal Configuration > CPU Thermal Configuration | Tcc Activation Offset | 0 … 63 (step 0) | 5 | `CpuSetup` @ `0x07a` (1) |
| Advanced > Thermal Configuration > CPU Thermal Configuration | Tcc Offset Time Window | Disabled (0x0) \| 5 ms (0x5) \| 10 ms (0xa) \| 55 ms (0x37) \| 156 ms (0x9c) \| 375 ms (0x177) \| 500 ms (0x1f4) \| 750 ms (0x2ee) \| 1 sec… | Disabled | `CpuSetup` @ `0x188` (4) |
| Advanced > Thermal Configuration > CPU Thermal Configuration | Tcc Offset Clamp Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x18c` (1) |
| Advanced > Thermal Configuration > CPU Thermal Configuration | Tcc Offset Lock Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x18d` (1) |
| Advanced > Thermal Configuration > CPU Thermal Configuration | Bi-directional PROCHOT# | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x075` (1) |
| Advanced > Thermal Configuration > CPU Thermal Configuration | Disable PROCHOT# Output | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x076` (1) |
| Advanced > Thermal Configuration > CPU Thermal Configuration | Disable VR Thermal Alert | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x077` (1) |
| Advanced > Thermal Configuration > CPU Thermal Configuration | PROCHOT Response | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x079` (1) |
| Advanced > Thermal Configuration > CPU Thermal Configuration | PROCHOT Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x078` (1) |
| Advanced > Thermal Configuration > CPU Thermal Configuration | ACPI T-States | Disabled (0) \| Enabled (1) | 0 | `CpuSetup` @ `0x074` (1) |
| Advanced > Thermal Configuration > CPU Thermal Configuration | PECI Reset | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x236` (1) |
| Advanced > Thermal Configuration > CPU Thermal Configuration | PECI C10 Reset | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x235` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Intel(R) Dynamic Tuning | Disabled (0x0) \| Enabled (0x1) | 1 | `Setup` @ `0x3a8` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Processor Thermal Device | Disabled (0x0) \| SA Thermal Device (0x1) | SA Thermal Device | `Setup` @ `0x3aa` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Active Thermal Trip Point | 0 … 127 (step 1) | 0 | `Setup` @ `0x3ab` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Passive Thermal Trip Point | 0 … 127 (step 1) | 0 | `Setup` @ `0x3ac` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Critical Thermal Trip Point | 0 … 127 (step 1) | 0 | `Setup` @ `0x3ad` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | S3/CS Thermal Trip Point | 0 … 127 (step 1) | 0 | `Setup` @ `0x3ae` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Hot Thermal Trip Point | 0 … 127 (step 1) | 0 | `Setup` @ `0x3b0` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Thermal Sampling Period | 0 … 100 (step 1) | 0 | `Setup` @ `0x3af` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | PPCC Step Size | 0.5 Watts (0x1f4) \| 1.0 Watts (0x3e8) \| 1.5 Watts (0x5dc) \| 2.0 Watts (0x7d0) | 0.5 Watts | `Setup` @ `0x3b1` (4) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Minimum Power Limit (cTDP Nom) | 0 … 30000 (step 125) | 125 | `Setup` @ `0x3ba` (2) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Minimum Power Limit (cTDP Down) | 0 … 30000 (step 125) | 125 | `Setup` @ `0x3bc` (2) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Minimum Power Limit (cTDP up) | 0 … 30000 (step 125) | 125 | `Setup` @ `0x3be` (2) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | CLPO Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x3b5` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | CLPO Start PState | 0 … 16 (step 1) | 16 | `Setup` @ `0x3b6` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | CLPO Step Size | 0 … 100 (step 1) | 50 | `Setup` @ `0x3b7` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | CLPO Power Control | Disabled (0x0) \| SMT Off lining (0x1) \| Core Off lining (0x2) | SMT Off lining | `Setup` @ `0x3b8` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | CLPO Performance Control | Disabled (0x0) \| SMT Off lining (0x1) \| Core Off lining (0x2) | Core Off lining | `Setup` @ `0x3b9` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | ConfigTDP | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3c0` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Intel(R) Dynamic Tuning Configuration | 0 … 255 (step 1) | 15 | `Setup` @ `0x3a9` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | FAN1 Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3c1` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Display participant | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3c2` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Display Low Limit | 0 … 100 (step 1) | 30 | `Setup` @ `0x3c4` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Display High Limit | 0 … 100 (step 1) | 100 | `Setup` @ `0x3c3` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Wireless participant | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3c5` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Active Thermal Trip Point | 0 … 127 (step 1) | 63 | `Setup` @ `0x3c6` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Passive Thermal Trip Point | 0 … 127 (step 1) | 71 | `Setup` @ `0x3c7` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Critical Thermal Trip Point | 0 … 127 (step 1) | 100 | `Setup` @ `0x3c8` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | S3/CS Thermal Trip Point | 0 … 127 (step 1) | 90 | `Setup` @ `0x3c9` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Hot Thermal Trip Point | 0 … 127 (step 1) | 95 | `Setup` @ `0x3ca` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Thermal Sampling Period | 0 … 100 (step 1) | 0 | `Setup` @ `0x3cb` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | WWAN participant | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3cc` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Active Thermal Trip Point | 0 … 127 (step 1) | 63 | `Setup` @ `0x3cd` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Passive Thermal Trip Point | 0 … 127 (step 1) | 71 | `Setup` @ `0x3ce` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Critical Thermal Trip Point | 0 … 127 (step 1) | 100 | `Setup` @ `0x3cf` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | S3/CS Thermal Trip Point | 0 … 127 (step 1) | 90 | `Setup` @ `0x3d0` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Hot Thermal Trip Point | 0 … 127 (step 1) | 95 | `Setup` @ `0x3d1` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Charger participant | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3d2` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Power participant | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3d3` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | 2D Camera participant | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3d6` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Battery Participant | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x65d` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Intel Dynamic Tuning Battery Sampling Period | 0 … 1000 (step 1) | 0 | `Setup` @ `0x3d4` (2) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Storage participant1 | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3d7` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Active Thermal Trip Point | 0 … 127 (step 1) | 63 | `Setup` @ `0x3d8` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Passive Thermal Trip Point | 0 … 127 (step 1) | 71 | `Setup` @ `0x3d9` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Critical Thermal Trip Point | 0 … 127 (step 1) | 100 | `Setup` @ `0x3da` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | S3/CS Thermal Trip Point | 0 … 127 (step 1) | 90 | `Setup` @ `0x3db` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Hot Thermal Trip Point | 0 … 127 (step 1) | 95 | `Setup` @ `0x3dc` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Storage participant2 | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3dd` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Active Thermal Trip Point | 0 … 127 (step 1) | 63 | `Setup` @ `0x3de` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Passive Thermal Trip Point | 0 … 127 (step 1) | 71 | `Setup` @ `0x3df` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Critical Thermal Trip Point | 0 … 127 (step 1) | 100 | `Setup` @ `0x3e0` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | S3/CS Thermal Trip Point | 0 … 127 (step 1) | 90 | `Setup` @ `0x3e1` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Hot Thermal Trip Point | 0 … 127 (step 1) | 95 | `Setup` @ `0x3e2` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Virtual Sensor participant 1 | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3e3` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Active Thermal Trip Point | 0 … 127 (step 1) | 50 | `Setup` @ `0x3e4` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Passive Thermal Trip Point | 0 … 127 (step 1) | 50 | `Setup` @ `0x3e5` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Critical Thermal Trip Point | 0 … 127 (step 1) | 70 | `Setup` @ `0x3e6` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Hot Thermal Trip Point | 0 … 127 (step 1) | 65 | `Setup` @ `0x3e8` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | S3/CS Thermal Trip Point | 0 … 127 (step 1) | 60 | `Setup` @ `0x3e7` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Virtual Sensor participant 2 | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3e9` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Active Thermal Trip Point | 0 … 127 (step 1) | 50 | `Setup` @ `0x3ea` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Passive Thermal Trip Point | 0 … 127 (step 1) | 50 | `Setup` @ `0x3eb` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Critical Thermal Trip Point | 0 … 127 (step 1) | 70 | `Setup` @ `0x3ec` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Hot Thermal Trip Point | 0 … 127 (step 1) | 65 | `Setup` @ `0x3ee` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | S3/CS Thermal Trip Point | 0 … 127 (step 1) | 60 | `Setup` @ `0x3ed` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Sensor Device 1 | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3f0` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Active Thermal Trip Point | 0 … 127 (step 1) | 63 | `Setup` @ `0x3f1` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Passive Thermal Trip Point | 0 … 127 (step 1) | 71 | `Setup` @ `0x3f2` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Critical Thermal Trip Point | 0 … 127 (step 1) | 103 | `Setup` @ `0x3f3` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | S3/CS Thermal Trip Point | 0 … 127 (step 1) | 97 | `Setup` @ `0x3f4` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Hot Thermal Trip Point | 0 … 127 (step 1) | 100 | `Setup` @ `0x3f5` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Thermal Sampling Period | 0 … 100 (step 1) | 0 | `Setup` @ `0x3f6` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Sensor Device 2 | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x3f7` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Active Thermal Trip Point | 0 … 127 (step 1) | 0 | `Setup` @ `0x3f8` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Passive Thermal Trip Point | 0 … 127 (step 1) | 0 | `Setup` @ `0x3f9` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Critical Thermal Trip Point | 0 … 127 (step 1) | 0 | `Setup` @ `0x3fa` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | S3/CS Thermal Trip Point | 0 … 127 (step 1) | 0 | `Setup` @ `0x3fb` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Hot Thermal Trip Point | 0 … 127 (step 1) | 0 | `Setup` @ `0x3fc` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Thermal Sampling Period | 0 … 100 (step 1) | 0 | `Setup` @ `0x3fd` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Sensor Device 3 | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3fe` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Active Thermal Trip Point | 0 … 127 (step 1) | 60 | `Setup` @ `0x3ff` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Passive Thermal Trip Point | 0 … 127 (step 1) | 65 | `Setup` @ `0x400` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Critical Thermal Trip Point | 0 … 127 (step 1) | 80 | `Setup` @ `0x401` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | S3/CS Thermal Trip Point | 0 … 127 (step 1) | 70 | `Setup` @ `0x402` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Hot Thermal Trip Point | 0 … 127 (step 1) | 75 | `Setup` @ `0x403` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Thermal Sampling Period | 0 … 100 (step 1) | 0 | `Setup` @ `0x404` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Sensor Device 4 | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x405` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Active Thermal Trip Point | 0 … 127 (step 1) | 60 | `Setup` @ `0x406` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Passive Thermal Trip Point | 0 … 127 (step 1) | 65 | `Setup` @ `0x407` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Critical Thermal Trip Point | 0 … 127 (step 1) | 80 | `Setup` @ `0x408` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | S3/CS Thermal Trip Point | 0 … 127 (step 1) | 70 | `Setup` @ `0x409` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Hot Thermal Trip Point | 0 … 127 (step 1) | 75 | `Setup` @ `0x40a` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Thermal Sampling Period | 0 … 100 (step 1) | 0 | `Setup` @ `0x40b` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Sensor Device 5 | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x40c` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Active Thermal Trip Point | 0 … 127 (step 1) | 60 | `Setup` @ `0x40d` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Passive Thermal Trip Point | 0 … 127 (step 1) | 65 | `Setup` @ `0x40e` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Critical Thermal Trip Point | 0 … 127 (step 1) | 80 | `Setup` @ `0x40f` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | S3/CS Thermal Trip Point | 0 … 127 (step 1) | 70 | `Setup` @ `0x410` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Hot Thermal Trip Point | 0 … 127 (step 1) | 75 | `Setup` @ `0x411` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration | Thermal Sampling Period | 0 … 100 (step 1) | 0 | `Setup` @ `0x412` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration > OEM variable and Object | Design Variable 0 | 0 … 255 (step 1) | 0 | `Setup` @ `0x420` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration > OEM variable and Object | Design Variable 1 | 0 … 255 (step 1) | 0 | `Setup` @ `0x421` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration > OEM variable and Object | Design Variable 2 | 0 … 255 (step 1) | 0 | `Setup` @ `0x422` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration > OEM variable and Object | Design Variable 3 | 0 … 255 (step 1) | 0 | `Setup` @ `0x423` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration > OEM variable and Object | Design Variable 4 | 0 … 255 (step 1) | 0 | `Setup` @ `0x424` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration > OEM variable and Object | Design Variable 5 | 0 … 255 (step 1) | 0 | `Setup` @ `0x425` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration > OEM variable and Object | PPCC Object | Disabled (0x1) \| Enabled (0x0) | Enabled | `Setup` @ `0x413` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration > OEM variable and Object | PDRT Object | Disabled (0x1) \| Enabled (0x0) | Enabled | `Setup` @ `0x414` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration > OEM variable and Object | ARTG Object | Disabled (0x1) \| Enabled (0x0) | Enabled | `Setup` @ `0x415` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration > OEM variable and Object | PMAX Object | Disabled (0x1) \| Enabled (0x0) | Enabled | `Setup` @ `0x416` (1) |
| Advanced > Thermal Configuration > Intel(R) Dynamic Tuning Configuration > OEM variable and Object | _TMP 1 Object | Disabled (0x1) \| Enabled (0x0) | Disabled | `Setup` @ `0x417` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Automatic Thermal Reporting | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x1e6` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Critical Trip Point | 15 C (0xf) \| 23 C (0x17) \| 31 C (0x1f) \| 39 C (0x27) \| 47 C (0x2f) \| 55 C (0x37) \| 63 C (0x3f) \| 71 C (0x47) \| 79 C (0x4f) \| 87 C … | 119 | `Setup` @ `0x396` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Active Trip Point 0 | Disabled (0x7f) \| 15 C (0xf) \| 23 C (0x17) \| 31 C (0x1f) \| 39 C (0x27) \| 47 C (0x2f) \| 55 C (0x37) \| 63 C (0x3f) \| 71 C (0x47) \| 7… | 71 C | `Setup` @ `0x392` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Active Trip Point 0 Fan Speed | 0 … 100 (step 1) | 100 | `Setup` @ `0x394` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Active Trip Point 1 | Disabled (0x7f) \| 15 C (0xf) \| 23 C (0x17) \| 31 C (0x1f) \| 39 C (0x27) \| 47 C (0x2f) \| 55 C (0x37) \| 63 C (0x3f) \| 71 C (0x47) \| 7… | 55 C | `Setup` @ `0x391` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Active Trip Point 1 Fan Speed | 0 … 100 (step 1) | 75 | `Setup` @ `0x393` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Passive Trip Point | Disabled (0x7f) \| 15 C (0xf) \| 23 C (0x17) \| 31 C (0x1f) \| 39 C (0x27) \| 47 C (0x2f) \| 55 C (0x37) \| 63 C (0x3f) \| 71 C (0x47) \| 7… | 95 | `Setup` @ `0x395` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Passive TC1 Value | 1 … 16 (step 1) | 1 | `Setup` @ `0x397` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Passive TC2 Value | 1 … 16 (step 1) | 5 | `Setup` @ `0x398` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Passive TSP Value | 2 … 32 (step 2) | 10 | `Setup` @ `0x399` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Active Trip Points | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x39a` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Passive Trip Points | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x39b` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Critical Trip Points | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x39c` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | PCH Temp Read | Disabled (0) \| Enabled (1) | Enabled | `Setup` @ `0x3a2` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | CPU Energy Read | Disabled (0) \| Enabled (1) | Enabled | `Setup` @ `0x3a1` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | CPU Temp Read | Disabled (0) \| Enabled (1) | Enabled | `Setup` @ `0x3a0` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | Alert Enable Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3a3` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | PCH Alert | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3a4` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | DIMM Alert | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x3a5` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | CPU Temp | 1 … 110 (step 1) | 90 | `Setup` @ `0x3a6` (1) |
| Advanced > Thermal Configuration > Platform Thermal Configuration | CPU Fan Speed | 1 … 100 (step 1) | 65 | `Setup` @ `0x3a7` (1) |
