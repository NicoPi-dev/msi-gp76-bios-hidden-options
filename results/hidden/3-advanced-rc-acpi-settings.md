# Advanced > RC ACPI Settings

Category: **Hidden - MSI advanced menu** - 42 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > RC ACPI Settings | PTID Support | Disabled (0) \| Enabled (1) | Enabled | `Setup` @ `0x007` (1) |
| Advanced > RC ACPI Settings | PECI Access Method | Direct I/O (0x0) \| ACPI (0x1) | Direct I/O | `Setup` @ `0x013` (1) |
| Advanced > RC ACPI Settings | Native PCIE Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x005` (1) |
| Advanced > RC ACPI Settings | Native ASPM | Auto (0x2) \| Enabled (0x1) \| Disabled (0x0) | Disabled | `Setup` @ `0x006` (1) |
| Advanced > RC ACPI Settings | Wake System from S5 | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x00e` (1) |
| Advanced > RC ACPI Settings | Low Power S0 Idle Capability | Disabled (0x0) \| Enabled (0x1) | 0 | `Setup` @ `0x014` (1) |
| Advanced > RC ACPI Settings | PUIS Enable | Enabled (0x1) \| Disabled (0x0) | Disabled | `Setup` @ `0x51e` (1) |
| Advanced > RC ACPI Settings | EC Notification | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x027` (1) |
| Advanced > RC ACPI Settings | EC CS Debug Light | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x028` (1) |
| Advanced > RC ACPI Settings | EC Low Power Mode | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x029` (1) |
| Advanced > RC ACPI Settings | Sensor Standby | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x038` (1) |
| Advanced > RC ACPI Settings | CS PL1 Limit | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x039` (1) |
| Advanced > RC ACPI Settings | CS PL1 Value | 3000 … 20000 (step 125) | 4500 | `Setup` @ `0x03a` (2) |
| Advanced > RC ACPI Settings | Lpit Residency Counter | SLP S0 (0x0) \| C10 (0x1) | SLP S0 | `Setup` @ `0x03c` (1) |
| Advanced > RC ACPI Settings | Intel Ready Mode Technology | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x03d` (1) |
| Advanced > RC ACPI Settings | HW Notification | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x003` (1) |
| Advanced > RC ACPI Settings | Intel RMT State | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x004` (1) |
| Advanced > RC ACPI Settings | PCI Delay Optimization | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x00d` (1) |
| Advanced > RC ACPI Settings | MSI enabled | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x4ae` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP CPU | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x015` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP Graphics | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x016` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP IPU | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x024` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP PEG0 | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x51a` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP SATA | No Constraint (0x0) \| Adapter D0/F1 (0x1) \| Raid Volume0 (0x2) \| Adapter D3 (0x3) | Adapter D0/F1 | `Setup` @ `0x017` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP enumerated SATA ports | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x65f` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP PCIe Storage | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x52e` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP PCIe DG1 | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x678` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP UART | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x018` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP I2C0 | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x019` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP I2C1 | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x01a` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP I2C2 | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x01b` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP I2C3 | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x01c` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP I2C4 | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x01d` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP I2C5 | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x01e` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP SPI | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x01f` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP XHCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x020` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP Audio | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x021` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP EMMC | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x022` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP SDXC | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x023` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP CSME | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x025` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP LAN(GBE) | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x026` (1) |
| Advanced > RC ACPI Settings > PEP Constraints Configuration | PEP TBT RP | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x66d` (1) |
