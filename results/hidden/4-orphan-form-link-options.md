# (orphan form) Link options

Category: **Hidden - permanently** - 168 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| (orphan form) Link options | Sensor Model | OV16860 (0xe) \| OV8856 (0xd) \| OV9234 (0xc) \| IMX135 (0x0) \| OV5693 (0x1) \| IMX179 (0x2) \| OV8858 (0x3) \| OV2740-IVCAM (0x4) \| OV97… | OV16860 | `Setup` @ `0x0f3` (1) |
| (orphan form) Link options | Custom HID |  |  | `Setup` @ `0x0f4` (1) |
| (orphan form) Link options | Lanes Clock division | 4 4 2 2 (0x0) \| 4 4 3 1 (0x2) \| 4 4 4 0 (0x3) \| 8 0 2 2 (0x4) \| 8 0 3 1 (0x6) \| 8 0 4 0 (0x7) | 4 4 2 2 | `Setup` @ `0x056` (1) |
| (orphan form) Link options | CRD Version | PTC (0x10) \| CRD-D (0x20) \| CRD-G (0x30) \| Kilshon-PPV (0x40) \| CRD-G2 (0x50) | CRD-G2 | `Setup` @ `0x14e` (1) |
| (orphan form) Link options | GPIO control | No Control Logic (0xff) \| Control Logic 1 (0x0) \| Control Logic 2 (0x1) \| Control Logic 3 (0x2) \| Control Logic 4 (0x3) | 0 | `Setup` @ `0x15a` (1) |
| (orphan form) Link options | Camera position | Front (0x61) \| Back (0x69) | Back | `Setup` @ `0x106` (1) |
| (orphan form) Link options | Flash Support | Driver default (0x0) \| Disabled (0x2) \| Enabled (0x3) | 3 | `Setup` @ `0x15b` (1) |
| (orphan form) Link options | Privacy LED | Driver default (0x0) \| ILEDA, 16mA (0x1) \| ILEDB, 2mA (0x2) \| ILEDB, 4mA (0x3) \| ILEDB, 8mA (0x4) \| ILEDB, 16mA (0x5) | Driver default | `Setup` @ `0x15c` (1) |
| (orphan form) Link options | Rotation | 0 (0x0) \| 90 (0x2) \| 180 (0x4) \| 270 (0x6) | 0 | `Setup` @ `0x15d` (1) |
| (orphan form) Link options | PMIC Position | Position 1 (0x0) \| Position 2 (0x1) | Position 1 | `Setup` @ `0x15e` (1) |
| (orphan form) Link options | Voltage Rail | 3 voltage rail (0x0) \| 2 voltage rail (0x1) | 3 voltage rail | `Setup` @ `0x15f` (1) |
| (orphan form) Link options | Camera module name |  |  | `Setup` @ `0x107` (1) |
| (orphan form) Link options | LaneUsed | x1 (0x1) \| x2 (0x2) \| x3 (0x3) \| x4 (0x4) \| x8 (0x8) | x4 | `Setup` @ `0x14f` (1) |
| (orphan form) Link options | MCLK | 6000000 … 27000000 (step 100000) | 19200000 | `Setup` @ `0x156` (4) |
| (orphan form) Link options | EEPROM Type | ROM_NONE (0x0) \| ROM_OTP (0x1) \| ROM_EEPROM_16K_64 (0x2) \| ROM_EEPROM_16K_16 (0x3) \| ROM_OTP_ACPI_ACPI (0x4) \| ROM_ACPI (0x5) \| ROM_E… | ROM_EEPROM_M24C64 | `Setup` @ `0x150` (1) |
| (orphan form) Link options | VCM Type | VCM_NONE (0x0) \| VCM_AD5823 (0x1) \| VCM_DW9714 (0x2) \| VCM_AD5816 (0x3) \| VCM_DW9719 (0x4) \| VCM_DW9718 (0x5) \| VCM_DW9806B (0x6) \| … | VCM_LC898212AXB | `Setup` @ `0x151` (1) |
| (orphan form) Link options | Number of I2C Components | 0 … 12 (step 1) | 3 | `Setup` @ `0x127` (1) |
| (orphan form) Link options | I2C Channel | I2C0 (0x0) \| I2C1 (0x1) \| I2C2 (0x2) \| I2C3 (0x3) \| I2C4 (0x4) \| I2C5 (0x5) | I2C2 | `Setup` @ `0x128` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 16 | `Setup` @ `0x129` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | Sensor | `Setup` @ `0x141` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 114 | `Setup` @ `0x12b` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | VCM | `Setup` @ `0x142` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 81 | `Setup` @ `0x12d` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM | `Setup` @ `0x143` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 81 | `Setup` @ `0x12f` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT1 | `Setup` @ `0x144` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 82 | `Setup` @ `0x131` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT2 | `Setup` @ `0x145` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 83 | `Setup` @ `0x133` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT3 | `Setup` @ `0x146` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 84 | `Setup` @ `0x135` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT4 | `Setup` @ `0x147` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 85 | `Setup` @ `0x137` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT5 | `Setup` @ `0x148` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 86 | `Setup` @ `0x139` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT6 | `Setup` @ `0x149` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 87 | `Setup` @ `0x13b` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT7 | `Setup` @ `0x14a` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 88 | `Setup` @ `0x13d` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | IO Expander | `Setup` @ `0x14b` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 89 | `Setup` @ `0x13f` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | Sensor | `Setup` @ `0x14c` (1) |
| (orphan form) Link options | Sensor Model | OV16860 (0xe) \| OV8856 (0xd) \| OV9234 (0xc) \| IMX135 (0x0) \| OV5693 (0x1) \| IMX179 (0x2) \| OV8858 (0x3) \| OV2740-IVCAM (0x4) \| OV97… | OV9234 | `Setup` @ `0x160` (1) |
| (orphan form) Link options | Custom HID |  |  | `Setup` @ `0x161` (1) |
| (orphan form) Link options | Lanes Clock division | 4 4 2 2 (0x0) \| 4 4 3 1 (0x2) \| 4 4 4 0 (0x3) \| 8 0 2 2 (0x4) \| 8 0 3 1 (0x6) \| 8 0 4 0 (0x7) | 4 4 2 2 | `Setup` @ `0x056` (1) |
| (orphan form) Link options | CRD Version | PTC (0x10) \| CRD-D (0x20) \| CRD-G (0x30) \| Kilshon-PPV (0x40) \| CRD-G2 (0x50) | CRD-G2 | `Setup` @ `0x1bb` (1) |
| (orphan form) Link options | GPIO control | No Control Logic (0xff) \| Control Logic 1 (0x0) \| Control Logic 2 (0x1) \| Control Logic 3 (0x2) \| Control Logic 4 (0x3) | 0 | `Setup` @ `0x1c7` (1) |
| (orphan form) Link options | Camera position | Front (0x61) \| Back (0x69) | Front | `Setup` @ `0x173` (1) |
| (orphan form) Link options | Flash Support | Driver default (0x0) \| Disabled (0x2) \| Enabled (0x3) | Enabled | `Setup` @ `0x1c8` (1) |
| (orphan form) Link options | Privacy LED | Driver default (0x0) \| ILEDA, 16mA (0x1) \| ILEDB, 2mA (0x2) \| ILEDB, 4mA (0x3) \| ILEDB, 8mA (0x4) \| ILEDB, 16mA (0x5) | Driver default | `Setup` @ `0x1c9` (1) |
| (orphan form) Link options | Rotation | 0 (0x0) \| 90 (0x2) \| 180 (0x4) \| 270 (0x6) | 0 | `Setup` @ `0x1ca` (1) |
| (orphan form) Link options | PMIC Position | Position 1 (0x0) \| Position 2 (0x1) | Position 2 | `Setup` @ `0x1cb` (1) |
| (orphan form) Link options | Voltage Rail | 3 voltage rail (0x0) \| 2 voltage rail (0x1) | 3 voltage rail | `Setup` @ `0x1cc` (1) |
| (orphan form) Link options | Camera module name |  |  | `Setup` @ `0x174` (1) |
| (orphan form) Link options | LaneUsed | x1 (0x1) \| x2 (0x2) \| x3 (0x3) \| x4 (0x4) | x1 | `Setup` @ `0x1bc` (1) |
| (orphan form) Link options | MCLK | 6000000 … 27000000 (step 100000) | 19200000 | `Setup` @ `0x1c3` (4) |
| (orphan form) Link options | EEPROM Type | ROM_NONE (0x0) \| ROM_OTP (0x1) \| ROM_EEPROM_16K_64 (0x2) \| ROM_EEPROM_16K_16 (0x3) \| ROM_OTP_ACPI_ACPI (0x4) \| ROM_ACPI (0x5) \| ROM_E… | ROM_NONE | `Setup` @ `0x1bd` (1) |
| (orphan form) Link options | VCM Type | VCM_NONE (0x0) \| VCM_AD5823 (0x1) \| VCM_DW9714 (0x2) \| VCM_AD5816 (0x3) \| VCM_DW9719 (0x4) \| VCM_DW9718 (0x5) \| VCM_DW9806B (0x6) \| … | VCM_NONE | `Setup` @ `0x1be` (1) |
| (orphan form) Link options | Number of I2C Components | 0 … 12 (step 1) | 1 | `Setup` @ `0x194` (1) |
| (orphan form) Link options | I2C Channel | I2C0 (0x0) \| I2C1 (0x1) \| I2C2 (0x2) \| I2C3 (0x3) \| I2C4 (0x4) \| I2C5 (0x5) | I2C2 | `Setup` @ `0x195` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 54 | `Setup` @ `0x196` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | Sensor | `Setup` @ `0x1ae` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 12 | `Setup` @ `0x198` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | VCM | `Setup` @ `0x1af` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 80 | `Setup` @ `0x19a` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM | `Setup` @ `0x1b0` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 81 | `Setup` @ `0x19c` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT1 | `Setup` @ `0x1b1` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 82 | `Setup` @ `0x19e` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT2 | `Setup` @ `0x1b2` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 83 | `Setup` @ `0x1a0` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT3 | `Setup` @ `0x1b3` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 84 | `Setup` @ `0x1a2` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT4 | `Setup` @ `0x1b4` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 85 | `Setup` @ `0x1a4` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT5 | `Setup` @ `0x1b5` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 86 | `Setup` @ `0x1a6` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT6 | `Setup` @ `0x1b6` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 87 | `Setup` @ `0x1a8` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT7 | `Setup` @ `0x1b7` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 88 | `Setup` @ `0x1aa` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | IO Expander | `Setup` @ `0x1b8` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 89 | `Setup` @ `0x1ac` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | Flash | `Setup` @ `0x1b9` (1) |
| (orphan form) Link options | Sensor Model | OV16860 (0xe) \| OV8856 (0xd) \| OV9234 (0xc) \| IMX135 (0x0) \| OV5693 (0x1) \| IMX179 (0x2) \| OV8858 (0x3) \| OV2740-IVCAM (0x4) \| OV97… | OV8856 | `Setup` @ `0x1cd` (1) |
| (orphan form) Link options | Custom HID |  |  | `Setup` @ `0x1ce` (1) |
| (orphan form) Link options | Lanes Clock division | 4 4 2 2 (0x0) \| 4 4 3 1 (0x2) \| 4 4 4 0 (0x3) \| 8 0 2 2 (0x4) \| 8 0 3 1 (0x6) \| 8 0 4 0 (0x7) | 4 4 2 2 | `Setup` @ `0x056` (1) |
| (orphan form) Link options | CRD Version | PTC (0x10) \| CRD-D (0x20) \| CRD-G (0x30) \| Kilshon-PPV (0x40) \| CRD-G2 (0x50) | CRD-D | `Setup` @ `0x228` (1) |
| (orphan form) Link options | GPIO control | No Control Logic (0xff) \| Control Logic 1 (0x0) \| Control Logic 2 (0x1) \| Control Logic 3 (0x2) \| Control Logic 4 (0x3) | 1 | `Setup` @ `0x234` (1) |
| (orphan form) Link options | Camera position | Front (0x61) \| Back (0x69) | Front | `Setup` @ `0x1e0` (1) |
| (orphan form) Link options | Flash Support | Driver default (0x0) \| Disabled (0x2) \| Enabled (0x3) | Disabled | `Setup` @ `0x235` (1) |
| (orphan form) Link options | Privacy LED | Driver default (0x0) \| ILEDA, 16mA (0x1) \| ILEDB, 2mA (0x2) \| ILEDB, 4mA (0x3) \| ILEDB, 8mA (0x4) \| ILEDB, 16mA (0x5) | Driver default | `Setup` @ `0x236` (1) |
| (orphan form) Link options | Rotation | 0 (0x0) \| 90 (0x2) \| 180 (0x4) \| 270 (0x6) | 0 | `Setup` @ `0x237` (1) |
| (orphan form) Link options | PMIC Position | Position 1 (0x0) \| Position 2 (0x1) | Position 1 | `Setup` @ `0x238` (1) |
| (orphan form) Link options | Voltage Rail | 3 voltage rail (0x0) \| 2 voltage rail (0x1) | 3 voltage rail | `Setup` @ `0x239` (1) |
| (orphan form) Link options | Camera module name |  |  | `Setup` @ `0x1e1` (1) |
| (orphan form) Link options | LaneUsed | x1 (0x1) \| x2 (0x2) \| x3 (0x3) \| x4 (0x4) | x4 | `Setup` @ `0x229` (1) |
| (orphan form) Link options | MCLK | 6000000 … 27000000 (step 100000) | 19200000 | `Setup` @ `0x230` (4) |
| (orphan form) Link options | EEPROM Type | ROM_NONE (0x0) \| ROM_OTP (0x1) \| ROM_EEPROM_16K_64 (0x2) \| ROM_EEPROM_16K_16 (0x3) \| ROM_OTP_ACPI_ACPI (0x4) \| ROM_ACPI (0x5) \| ROM_E… | ROM_OTP | `Setup` @ `0x22a` (1) |
| (orphan form) Link options | VCM Type | VCM_NONE (0x0) \| VCM_AD5823 (0x1) \| VCM_DW9714 (0x2) \| VCM_AD5816 (0x3) \| VCM_DW9719 (0x4) \| VCM_DW9718 (0x5) \| VCM_DW9806B (0x6) \| … | VCM_NONE | `Setup` @ `0x22b` (1) |
| (orphan form) Link options | Number of I2C Components | 0 … 12 (step 1) | 1 | `Setup` @ `0x201` (1) |
| (orphan form) Link options | I2C Channel | I2C0 (0x0) \| I2C1 (0x1) \| I2C2 (0x2) \| I2C3 (0x3) \| I2C4 (0x4) \| I2C5 (0x5) | I2C3 | `Setup` @ `0x202` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 16 | `Setup` @ `0x203` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | Sensor | `Setup` @ `0x21b` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 14 | `Setup` @ `0x205` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | VCM | `Setup` @ `0x21c` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 80 | `Setup` @ `0x207` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM | `Setup` @ `0x21d` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 81 | `Setup` @ `0x209` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT1 | `Setup` @ `0x21e` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 82 | `Setup` @ `0x20b` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT2 | `Setup` @ `0x21f` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 83 | `Setup` @ `0x20d` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT3 | `Setup` @ `0x220` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 84 | `Setup` @ `0x20f` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT4 | `Setup` @ `0x221` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 85 | `Setup` @ `0x211` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT5 | `Setup` @ `0x222` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 86 | `Setup` @ `0x213` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | Sensor | `Setup` @ `0x223` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 87 | `Setup` @ `0x215` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | Sensor | `Setup` @ `0x224` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 88 | `Setup` @ `0x217` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | Sensor | `Setup` @ `0x225` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 89 | `Setup` @ `0x219` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | Sensor | `Setup` @ `0x226` (1) |
| (orphan form) Link options | Sensor Model | OV16860 (0xe) \| OV8856 (0xd) \| OV9234 (0xc) \| IMX135 (0x0) \| OV5693 (0x1) \| IMX179 (0x2) \| OV8858 (0x3) \| OV2740-IVCAM (0x4) \| OV97… | OV9234 | `Setup` @ `0x23a` (1) |
| (orphan form) Link options | Custom HID |  |  | `Setup` @ `0x23b` (1) |
| (orphan form) Link options | Lanes Clock division | 4 4 2 2 (0x0) \| 4 4 3 1 (0x2) \| 4 4 4 0 (0x3) \| 8 0 2 2 (0x4) \| 8 0 3 1 (0x6) \| 8 0 4 0 (0x7) | 4 4 2 2 | `Setup` @ `0x056` (1) |
| (orphan form) Link options | CRD Version | PTC (0x10) \| CRD-D (0x20) \| CRD-G (0x30) \| Kilshon-PPV (0x40) \| CRD-G2 (0x50) | CRD-G2 | `Setup` @ `0x295` (1) |
| (orphan form) Link options | GPIO control | No Control Logic (0xff) \| Control Logic 1 (0x0) \| Control Logic 2 (0x1) \| Control Logic 3 (0x2) \| Control Logic 4 (0x3) | 0 | `Setup` @ `0x2a1` (1) |
| (orphan form) Link options | Camera position | Front (0x61) \| Back (0x69) | Front | `Setup` @ `0x24d` (1) |
| (orphan form) Link options | Flash Support | Driver default (0x0) \| Disabled (0x2) \| Enabled (0x3) | Enabled | `Setup` @ `0x2a2` (1) |
| (orphan form) Link options | Privacy LED | Driver default (0x0) \| ILEDA, 16mA (0x1) \| ILEDB, 2mA (0x2) \| ILEDB, 4mA (0x3) \| ILEDB, 8mA (0x4) \| ILEDB, 16mA (0x5) | Driver default | `Setup` @ `0x2a3` (1) |
| (orphan form) Link options | Rotation | 0 (0x0) \| 90 (0x2) \| 180 (0x4) \| 270 (0x6) | 0 | `Setup` @ `0x2a4` (1) |
| (orphan form) Link options | PMIC Position | Position 1 (0x0) \| Position 2 (0x1) | Position 2 | `Setup` @ `0x2a5` (1) |
| (orphan form) Link options | Voltage Rail | 3 voltage rail (0x0) \| 2 voltage rail (0x1) | 3 voltage rail | `Setup` @ `0x2a6` (1) |
| (orphan form) Link options | Camera module name |  |  | `Setup` @ `0x24e` (1) |
| (orphan form) Link options | LaneUsed | x1 (0x1) \| x2 (0x2) \| x3 (0x3) \| x4 (0x4) | x1 | `Setup` @ `0x296` (1) |
| (orphan form) Link options | MCLK | 6000000 … 27000000 (step 100000) | 19200000 | `Setup` @ `0x29d` (4) |
| (orphan form) Link options | EEPROM Type | ROM_NONE (0x0) \| ROM_OTP (0x1) \| ROM_EEPROM_16K_64 (0x2) \| ROM_EEPROM_16K_16 (0x3) \| ROM_OTP_ACPI_ACPI (0x4) \| ROM_ACPI (0x5) \| ROM_E… | ROM_NONE | `Setup` @ `0x297` (1) |
| (orphan form) Link options | VCM Type | VCM_NONE (0x0) \| VCM_AD5823 (0x1) \| VCM_DW9714 (0x2) \| VCM_AD5816 (0x3) \| VCM_DW9719 (0x4) \| VCM_DW9718 (0x5) \| VCM_DW9806B (0x6) \| … | VCM_NONE | `Setup` @ `0x298` (1) |
| (orphan form) Link options | Number of I2C Components | 0 … 12 (step 1) | 1 | `Setup` @ `0x26e` (1) |
| (orphan form) Link options | I2C Channel | I2C0 (0x0) \| I2C1 (0x1) \| I2C2 (0x2) \| I2C3 (0x3) \| I2C4 (0x4) \| I2C5 (0x5) | I2C2 | `Setup` @ `0x26f` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 54 | `Setup` @ `0x270` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | Sensor | `Setup` @ `0x288` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 12 | `Setup` @ `0x272` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | VCM | `Setup` @ `0x289` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 80 | `Setup` @ `0x274` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM | `Setup` @ `0x28a` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 81 | `Setup` @ `0x276` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT1 | `Setup` @ `0x28b` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 82 | `Setup` @ `0x278` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT2 | `Setup` @ `0x28c` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 83 | `Setup` @ `0x27a` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT3 | `Setup` @ `0x28d` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 84 | `Setup` @ `0x27c` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT4 | `Setup` @ `0x28e` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 85 | `Setup` @ `0x27e` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT5 | `Setup` @ `0x28f` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 86 | `Setup` @ `0x280` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT6 | `Setup` @ `0x290` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 87 | `Setup` @ `0x282` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | EEPROM_EXT7 | `Setup` @ `0x291` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 88 | `Setup` @ `0x284` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | IO Expander | `Setup` @ `0x292` (1) |
| (orphan form) Link options | I2C Address | 0 … 127 (step 1) | 89 | `Setup` @ `0x286` (2) |
| (orphan form) Link options | Device Type | Sensor (0x0) \| VCM (0x1) \| EEPROM (0x2) \| EEPROM_EXT1 (0x3) \| EEPROM_EXT2 (0x4) \| EEPROM_EXT3 (0x5) \| EEPROM_EXT4 (0x6) \| EEPROM_EXT… | Flash | `Setup` @ `0x293` (1) |
