# (orphan form) Control Logic options

Category: **Hidden - permanently** - 140 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| (orphan form) Control Logic options | Control Logic Type | Discrete (0x1) \| PMIC_TPS68470 (0x2) \| PMIC_UP6641 (0x3) \| PMIC_USER0 (0xfd) \| PMIC_USER1 (0xfe) | PMIC_TPS68470 | `Setup` @ `0x057` (1) |
| (orphan form) Control Logic options | CRD Version | PTC (0x10) \| CRD-D (0x20) \| CRD-G (0x30) \| Kilshon-PPV (0x40) \| CRD-G2 (0x50) | CRD-G2 | `Setup` @ `0x058` (1) |
| (orphan form) Control Logic options | Input Clock | 20 MHz (0x10) \| 24 MHz (0x20) \| 26 MHz (0x30) \| 19.2 MHz (0x40) | 20 MHz | `Setup` @ `0x059` (4) |
| (orphan form) Control Logic options | PCH Clock Source | IMGCLKOUT_0 (0x0) \| IMGCLKOUT_1 (0x1) | IMGCLKOUT_1 | `Setup` @ `0x05d` (1) |
| (orphan form) Control Logic options | PMIC Flash Panel | Front (0x21) \| Back (0x29) | 41 | `Setup` @ `0x062` (1) |
| (orphan form) Control Logic options | I2C Channel | I2C0 (0x0) \| I2C1 (0x1) \| I2C2 (0x2) \| I2C3 (0x3) \| I2C4 (0x4) \| I2C5 (0x5) | I2C2 | `Setup` @ `0x05f` (1) |
| (orphan form) Control Logic options | I2C Address | 0 … 127 (step 1) | 77 | `Setup` @ `0x060` (2) |
| (orphan form) Control Logic options | WLED1 Type | Disabled (0x0) \| White Led (0x1) \| Warm Led (0x2) \| IR Led (0x3) \| Xeon Led (0x4) | White Led | `Setup` @ `0x068` (1) |
| (orphan form) Control Logic options | WLED1 Flash Max Current | 0 … 31 (step 1) | 0 | `Setup` @ `0x063` (1) |
| (orphan form) Control Logic options | WLED1 Torch Max Current | 0 … 7 (step 1) | 0 | `Setup` @ `0x064` (1) |
| (orphan form) Control Logic options | WLED2 Type | Disabled (0x0) \| White Led (0x1) \| Warm Led (0x2) \| IR Led (0x3) \| Xeon Led (0x4) | IR Led | `Setup` @ `0x069` (1) |
| (orphan form) Control Logic options | WLED2 Flash Max Current | 0 … 31 (step 1) | 0 | `Setup` @ `0x065` (1) |
| (orphan form) Control Logic options | WLED2 Torch Max Current | 0 … 7 (step 1) | 0 | `Setup` @ `0x066` (1) |
| (orphan form) Control Logic options | SubPlatformId | 0 … 15 (step 1) | 0 | `Setup` @ `0x067` (1) |
| (orphan form) Control Logic options | Number of GPIO Pins | 0 … 4 (step 1) | 0 | `Setup` @ `0x05e` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 22 | `Setup` @ `0x06a` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x06e` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x072` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x076` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x07a` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 11 | `Setup` @ `0x06b` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x06f` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x073` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x077` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x07b` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 11 | `Setup` @ `0x06c` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x070` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Clock_En | `Setup` @ `0x074` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x078` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x07c` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 11 | `Setup` @ `0x06d` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x071` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x075` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x079` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x07d` (1) |
| (orphan form) Control Logic options | Control Logic Type | Discrete (0x1) \| PMIC_TPS68470 (0x2) \| PMIC_UP6641 (0x3) \| PMIC_USER0 (0xfd) \| PMIC_USER1 (0xfe) | Discrete | `Setup` @ `0x07e` (1) |
| (orphan form) Control Logic options | CRD Version | PTC (0x10) \| CRD-D (0x20) \| CRD-G (0x30) \| Kilshon-PPV (0x40) \| CRD-G2 (0x50) | CRD-D | `Setup` @ `0x07f` (1) |
| (orphan form) Control Logic options | Input Clock | 20 MHz (0x10) \| 24 MHz (0x20) \| 26 MHz (0x30) \| 19.2 MHz (0x40) | 20 MHz | `Setup` @ `0x080` (4) |
| (orphan form) Control Logic options | PCH Clock Source | IMGCLKOUT_0 (0x0) \| IMGCLKOUT_1 (0x1) | IMGCLKOUT_1 | `Setup` @ `0x084` (1) |
| (orphan form) Control Logic options | PMIC Flash Panel | Front (0x21) \| Back (0x29) | Back | `Setup` @ `0x089` (1) |
| (orphan form) Control Logic options | I2C Channel | I2C0 (0x0) \| I2C1 (0x1) \| I2C2 (0x2) \| I2C3 (0x3) \| I2C4 (0x4) \| I2C5 (0x5) | I2C3 | `Setup` @ `0x086` (1) |
| (orphan form) Control Logic options | I2C Address | 0 … 127 (step 1) | 73 | `Setup` @ `0x087` (2) |
| (orphan form) Control Logic options | WLED1 Type | Disabled (0x0) \| White Led (0x1) \| Warm Led (0x2) \| IR Led (0x3) \| Xeon Led (0x4) | Disabled | `Setup` @ `0x08f` (1) |
| (orphan form) Control Logic options | WLED1 Flash Max Current | 0 … 31 (step 1) | 0 | `Setup` @ `0x08a` (1) |
| (orphan form) Control Logic options | WLED1 Torch Max Current | 0 … 7 (step 1) | 0 | `Setup` @ `0x08b` (1) |
| (orphan form) Control Logic options | WLED2 Type | Disabled (0x0) \| White Led (0x1) \| Warm Led (0x2) \| IR Led (0x3) \| Xeon Led (0x4) | Disabled | `Setup` @ `0x090` (1) |
| (orphan form) Control Logic options | WLED2 Flash Max Current | 0 … 31 (step 1) | 0 | `Setup` @ `0x08c` (1) |
| (orphan form) Control Logic options | WLED2 Torch Max Current | 0 … 7 (step 1) | 0 | `Setup` @ `0x08d` (1) |
| (orphan form) Control Logic options | SubPlatformId | 0 … 15 (step 1) | 0 | `Setup` @ `0x08e` (1) |
| (orphan form) Control Logic options | Number of GPIO Pins | 0 … 4 (step 1) | 2 | `Setup` @ `0x085` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 22 | `Setup` @ `0x091` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | H | `Setup` @ `0x095` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x099` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x09d` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x0a1` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 16 | `Setup` @ `0x092` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | A | `Setup` @ `0x096` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Power_En | `Setup` @ `0x09a` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x09e` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x0a2` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 11 | `Setup` @ `0x093` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x097` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x09b` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x09f` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x0a3` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 11 | `Setup` @ `0x094` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x098` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x09c` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x0a0` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x0a4` (1) |
| (orphan form) Control Logic options | Control Logic Type | Discrete (0x1) \| PMIC_TPS68470 (0x2) \| PMIC_UP6641 (0x3) \| PMIC_USER0 (0xfd) \| PMIC_USER1 (0xfe) | PMIC_TPS68470 | `Setup` @ `0x0a5` (1) |
| (orphan form) Control Logic options | CRD Version | PTC (0x10) \| CRD-D (0x20) \| CRD-G (0x30) \| Kilshon-PPV (0x40) \| CRD-G2 (0x50) | CRD-G2 | `Setup` @ `0x0a6` (1) |
| (orphan form) Control Logic options | Input Clock | 20 MHz (0x10) \| 24 MHz (0x20) \| 26 MHz (0x30) \| 19.2 MHz (0x40) | 20 MHz | `Setup` @ `0x0a7` (4) |
| (orphan form) Control Logic options | PCH Clock Source | IMGCLKOUT_0 (0x0) \| IMGCLKOUT_1 (0x1) | IMGCLKOUT_0 | `Setup` @ `0x0ab` (1) |
| (orphan form) Control Logic options | PMIC Flash Panel | Front (0x21) \| Back (0x29) | Back | `Setup` @ `0x0b0` (1) |
| (orphan form) Control Logic options | I2C Channel | I2C0 (0x0) \| I2C1 (0x1) \| I2C2 (0x2) \| I2C3 (0x3) \| I2C4 (0x4) \| I2C5 (0x5) | I2C2 | `Setup` @ `0x0ad` (1) |
| (orphan form) Control Logic options | I2C Address | 0 … 127 (step 1) | 77 | `Setup` @ `0x0ae` (2) |
| (orphan form) Control Logic options | WLED1 Type | Disabled (0x0) \| White Led (0x1) \| Warm Led (0x2) \| IR Led (0x3) \| Xeon Led (0x4) | White Led | `Setup` @ `0x0b6` (1) |
| (orphan form) Control Logic options | WLED1 Flash Max Current | 0 … 31 (step 1) | 0 | `Setup` @ `0x0b1` (1) |
| (orphan form) Control Logic options | WLED1 Torch Max Current | 0 … 7 (step 1) | 0 | `Setup` @ `0x0b2` (1) |
| (orphan form) Control Logic options | WLED2 Type | Disabled (0x0) \| White Led (0x1) \| Warm Led (0x2) \| IR Led (0x3) \| Xeon Led (0x4) | IR Led | `Setup` @ `0x0b7` (1) |
| (orphan form) Control Logic options | WLED2 Flash Max Current | 0 … 31 (step 1) | 0 | `Setup` @ `0x0b3` (1) |
| (orphan form) Control Logic options | WLED2 Torch Max Current | 0 … 7 (step 1) | 0 | `Setup` @ `0x0b4` (1) |
| (orphan form) Control Logic options | SubPlatformId | 0 … 15 (step 1) | 0 | `Setup` @ `0x0b5` (1) |
| (orphan form) Control Logic options | Number of GPIO Pins | 0 … 4 (step 1) | 0 | `Setup` @ `0x0ac` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 22 | `Setup` @ `0x0b8` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x0bc` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x0c0` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x0c4` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x0c8` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 11 | `Setup` @ `0x0b9` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x0bd` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x0c1` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x0c5` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x0c9` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 11 | `Setup` @ `0x0ba` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x0be` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x0c2` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x0c6` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x0ca` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 11 | `Setup` @ `0x0bb` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x0bf` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x0c3` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x0c7` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x0cb` (1) |
| (orphan form) Control Logic options | Control Logic Type | Discrete (0x1) \| PMIC_TPS68470 (0x2) \| PMIC_UP6641 (0x3) \| PMIC_USER0 (0xfd) \| PMIC_USER1 (0xfe) | PMIC_TPS68470 | `Setup` @ `0x0cc` (1) |
| (orphan form) Control Logic options | CRD Version | PTC (0x10) \| CRD-D (0x20) \| CRD-G (0x30) \| Kilshon-PPV (0x40) \| CRD-G2 (0x50) | CRD-G2 | `Setup` @ `0x0cd` (1) |
| (orphan form) Control Logic options | Input Clock | 20 MHz (0x10) \| 24 MHz (0x20) \| 26 MHz (0x30) \| 19.2 MHz (0x40) | 20 MHz | `Setup` @ `0x0ce` (4) |
| (orphan form) Control Logic options | PCH Clock Source | IMGCLKOUT_0 (0x0) \| IMGCLKOUT_1 (0x1) | IMGCLKOUT_0 | `Setup` @ `0x0d2` (1) |
| (orphan form) Control Logic options | PMIC Flash Panel | Front (0x21) \| Back (0x29) | Back | `Setup` @ `0x0d7` (1) |
| (orphan form) Control Logic options | I2C Channel | I2C0 (0x0) \| I2C1 (0x1) \| I2C2 (0x2) \| I2C3 (0x3) \| I2C4 (0x4) \| I2C5 (0x5) | I2C2 | `Setup` @ `0x0d4` (1) |
| (orphan form) Control Logic options | I2C Address | 0 … 127 (step 1) | 77 | `Setup` @ `0x0d5` (2) |
| (orphan form) Control Logic options | WLED1 Type | Disabled (0x0) \| White Led (0x1) \| Warm Led (0x2) \| IR Led (0x3) \| Xeon Led (0x4) | White Led | `Setup` @ `0x0dd` (1) |
| (orphan form) Control Logic options | WLED1 Flash Max Current | 0 … 31 (step 1) | 0 | `Setup` @ `0x0d8` (1) |
| (orphan form) Control Logic options | WLED1 Torch Max Current | 0 … 7 (step 1) | 0 | `Setup` @ `0x0d9` (1) |
| (orphan form) Control Logic options | WLED2 Type | Disabled (0x0) \| White Led (0x1) \| Warm Led (0x2) \| IR Led (0x3) \| Xeon Led (0x4) | IR Led | `Setup` @ `0x0de` (1) |
| (orphan form) Control Logic options | WLED2 Flash Max Current | 0 … 31 (step 1) | 0 | `Setup` @ `0x0da` (1) |
| (orphan form) Control Logic options | WLED2 Torch Max Current | 0 … 7 (step 1) | 0 | `Setup` @ `0x0db` (1) |
| (orphan form) Control Logic options | SubPlatformId | 0 … 15 (step 1) | 0 | `Setup` @ `0x0dc` (1) |
| (orphan form) Control Logic options | Number of GPIO Pins | 0 … 4 (step 1) | 0 | `Setup` @ `0x0d3` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 22 | `Setup` @ `0x0df` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x0e3` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x0e7` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x0eb` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x0ef` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 11 | `Setup` @ `0x0e0` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x0e4` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x0e8` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x0ec` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x0f0` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 11 | `Setup` @ `0x0e1` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x0e5` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x0e9` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x0ed` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x0f1` (1) |
| (orphan form) Control Logic options | Group Pad Number | 0 … 23 (step 1) | 11 | `Setup` @ `0x0e2` (1) |
| (orphan form) Control Logic options | Group Number | A (0x0) \| B (0x1) \| C (0x2) \| D (0x3) \| E (0x4) \| F (0x5) \| G (0x6) \| H (0x7) | D | `Setup` @ `0x0e6` (1) |
| (orphan form) Control Logic options | Function | Reset (0x0) \| Power_En (0xb) \| Clock_En (0xc) \| pLED_En (0xd) | Reset | `Setup` @ `0x0ea` (1) |
| (orphan form) Control Logic options | Active Value | 0 … 1 (step 1) | 1 | `Setup` @ `0x0ee` (1) |
| (orphan form) Control Logic options | Initial Value | 0 … 1 (step 1) | 0 | `Setup` @ `0x0f2` (1) |
