# Advanced > PCH-IO Configuration

Category: **Hidden - MSI advanced menu** - 1547 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > PCH-IO Configuration | PCH LAN Controller | Enabled (0x1) \| Disabled (0x0) | Enabled | `PchSetup` @ `0x009` (1) |
| Advanced > PCH-IO Configuration | LAN Wake From DeepSx | Enabled (0x1) \| Disabled (0x0) | Enabled | `PchSetup` @ `0x005` (1) |
| Advanced > PCH-IO Configuration | Wake on LAN Enable | Enabled (0x1) \| Disabled (0x0) | Enabled | `PchSetup` @ `0x00c` (1) |
| Advanced > PCH-IO Configuration | SLP_LAN# Low on DC Power | Enabled (0x1) \| Disabled (0x0) | Enabled | `PchSetup` @ `0x00d` (1) |
| Advanced > PCH-IO Configuration | Disqualify GBE Disconnect And ModPhy PG | Enabled (0x1) \| Disabled (0x0) | Disabled | `PchSetup` @ `0x6e4` (1) |
| Advanced > PCH-IO Configuration | Sensor Hub Type | None (0x0) \| I2C Sensor Hub (0x1) \| USB Sensor Hub (0x2) | None | `Setup` @ `0x044` (1) |
| Advanced > PCH-IO Configuration | DeepSx Power Policies | Disabled (0x0) \| Enabled in S4-S5/Battery (0x3) \| Enabled in S4-S5 (0x4) | Disabled | `PchSetup` @ `0x004` (1) |
| Advanced > PCH-IO Configuration | PS_ON Enable | Enabled (0x1) \| Disabled (0x0) | Disabled | `PchSetup` @ `0x019` (1) |
| Advanced > PCH-IO Configuration | Wake on WLAN and BT Enable | Enabled (0x1) \| Disabled (0x0) | Disabled | `PchSetup` @ `0x00e` (1) |
| Advanced > PCH-IO Configuration | DeepSx Wake on WLAN and BT Enable | Enabled (0x1) \| Disabled (0x0) | Disabled | `PchSetup` @ `0x00f` (1) |
| Advanced > PCH-IO Configuration | Disable DSX ACPRESENT PullDown | Enabled (0x1) \| Disabled (0x0) | 0 | `PchSetup` @ `0x006` (1) |
| Advanced > PCH-IO Configuration | CLKRUN# logic | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x010` (1) |
| Advanced > PCH-IO Configuration | Serial IRQ Mode | Quiet (0x0) \| Continuous (0x1) | 1 | `PchSetup` @ `0x01e` (1) |
| Advanced > PCH-IO Configuration | State After G3 | S0 State (0x0) \| S5 State (0x1) | S5 State | `PchSetup` @ `0x01b` (1) |
| Advanced > PCH-IO Configuration | Port 80h Redirection | LPC Bus (0x0) \| PCIE Bus (0x1) | LPC Bus | `PchSetup` @ `0x01c` (1) |
| Advanced > PCH-IO Configuration | Enhance Port 80h LPC Decoding | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x01d` (1) |
| Advanced > PCH-IO Configuration | Compatible Revision ID | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x015` (1) |
| Advanced > PCH-IO Configuration | Legacy IO Low Latency | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x6e9` (1) |
| Advanced > PCH-IO Configuration | PCH Cross Throttling | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x67d` (1) |
| Advanced > PCH-IO Configuration | PCH Energy Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x011` (1) |
| Advanced > PCH-IO Configuration | Enable TCO Timer | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x014` (1) |
| Advanced > PCH-IO Configuration | Pcie Pll SSC | Auto (0xff) \| 0.0% (0x0) \| 0.1% (0x1) \| 0.2% (0x2) \| 0.3% (0x3) \| 0.4% (0x4) \| 0.5% (0x5) \| 0.6% (0x6) \| 0.7% (0x7) \| 0.8% (0x8) \… | Auto | `PchSetup` @ `0x01f` (1) |
| Advanced > PCH-IO Configuration | IOAPIC 24-119 Entries | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x67c` (1) |
| Advanced > PCH-IO Configuration | Enable 8254 Clock Gate | Disabled (0x0) \| Enabled (0x1) \| Enabled In Runtime and S3 Resume (0x2) | Enabled | `PchSetup` @ `0x6e6` (1) |
| Advanced > PCH-IO Configuration | Flash Protection Range Registers (FPRR) | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x6dd` (1) |
| Advanced > PCH-IO Configuration | SPD Write Disable | TRUE (0x1) \| FALSE (0x0) | TRUE | `PchSetup` @ `0x6db` (1) |
| Advanced > PCH-IO Configuration | LGMR | Enabled (0x1) \| Disabled (0x0) | Disabled | `PchSetup` @ `0x6da` (1) |
| Advanced > PCH-IO Configuration | Teton Glacier Mode | Dynamic Configuration for Teton Glacier Enable (0x1) \| Disabled (0x0) | Disabled | `PchSetup` @ `0x6e8` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | HD Audio | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Enabled | `PchSetup` @ `0x557` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | Audio DSP | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x558` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | Audio DSP Compliance Mode | Non-UAA (IntelSST) (0x0) \| UAA (HDA Inbox/IntelSST) (0x1) | Non-UAA (IntelSST) | `PchSetup` @ `0x559` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | Audio Link Mode | HD Audio Link (0x0) \| SSP (I2S) (0x1) \| SoundWire (0x2) \| Advanced Link Config (0x3) | HD Audio Link | `PchSetup` @ `0x55c` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | HDA Link | Disabled (0) \| Enabled (1) | 1 | `PchSetup` @ `0x55d` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | DMIC #0 | Disabled (0) \| Enabled (1) | 1 | `PchSetup` @ `0x55e` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | DMIC #1 | Disabled (0) \| Enabled (1) | 1 | `PchSetup` @ `0x55f` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | SSP #0 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x560` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | SSP #1 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x561` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | SSP #2 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x562` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | SSP #3 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x563` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | SSP #4 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x564` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | SSP #5 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x565` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | SNDW #1 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x566` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | SNDW #2 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x567` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | SNDW #3 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x568` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | SNDW #4 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x569` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration | HDA-Link Codec Select | Platform Onboard (0x0) \| External Kit (0x1) | Platform Onboard | `PchSetup` @ `0x56f` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio Advanced Configuration | iDisplay Audio Disconnect | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x55a` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio Advanced Configuration | Codec Sx Wake Capability | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x56d` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio Advanced Configuration | PME Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x55b` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio Advanced Configuration | SoundWire Buffer RCOMP Setting | Non-ACT Topology (0x0) \| ACT Topology (0x1) | Non-ACT Topology | `PchSetup` @ `0x56e` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio Advanced Configuration | HD Audio Link Frequency | 6 MHz (0x0) \| 12 MHz (0x1) \| 24 MHz (0x2) | 24 MHz | `PchSetup` @ `0x56a` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio Advanced Configuration | iDisplay Audio Link Frequency | 48 MHz (0x3) \| 96 MHz (0x4) | 96 MHz | `PchSetup` @ `0x56b` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio Advanced Configuration | iDisplay Audio Link T-Mode | 2T Mode (0x0) \| 1T Mode (0x1) | 2T Mode | `PchSetup` @ `0x56c` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | NHLT External Table | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x574` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | DMIC | Disabled (0x0) \| 1 Mic Array (0x3) \| 2 Mic Array (0x1) \| 4 Mic Array (0x2) | 2 | `PchSetup` @ `0x571` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Bluetooth | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x572` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | I2S | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x573` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | I2S Codec Select | Disabled (0x0) \| Realtek ALC274 (0x1) | Disabled | `PchSetup` @ `0x570` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | WoV (Wake on Voice) | Disabled (0) \| Enabled (1) | 0 | `PchSetup` @ `0x575` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Bluetooth Sideband | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x576` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | BT Intel HFP | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x57a` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | BT Intel A2DP | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x57b` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Codec based VAD | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x577` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | DSP based Speech  Pre-Processing Disabled | Disabled (0) \| Enabled (1) | 0 | `PchSetup` @ `0x57c` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Voice Activity Detection | Intel Wake on Voice (0x0) \| Windows 10 Voice Activation (0x1) | Intel Wake on Voice | `PchSetup` @ `0x57d` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Waves Post-process | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x57e` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | DTS | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x57f` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | IntelSST Speech | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x580` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Dolby | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x581` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Waves Pre-process | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x582` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Audyssey | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x583` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Maxim Smart AMP | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x584` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | ForteMedia SAMSoft | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x585` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Intel WoV | Disabled (0) \| Enabled (1) | 0 | `PchSetup` @ `0x586` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Sound Research IP | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x587` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Conexant Pre-Process | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x588` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Conexant Smart Amp | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x589` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Realtek Post-Process | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x58a` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Realtek Smart Amp | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x58b` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Icepower IP MFX sub module | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x58c` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Icepower IP EFX sub module | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x58d` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Icepower IP SFX sub module | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x58e` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Voice Preprocessing | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x58f` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Custom Module 'Alpha' | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x59b` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | 'Alpha' GUID: |  |  | `PchSetup` @ `0x59e` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Custom Module 'Beta' | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x59c` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | 'Beta'  GUID: |  |  | `PchSetup` @ `0x5e8` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | Custom Module 'Gamma' | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x59d` (1) |
| Advanced > PCH-IO Configuration > HD Audio Configuration > HD Audio DSP Features Configuration | 'Gamma' GUID: |  |  | `PchSetup` @ `0x632` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | ISH Controller | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x683` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | PDT Unlock Message | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x692` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | SPI | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x684` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | UART0 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x685` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | UART1 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x686` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | I2C0 | Disabled (0) \| Enabled (1) | Enabled | `PchSetup` @ `0x687` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | I2C1 | Disabled (0) \| Enabled (1) | Enabled | `PchSetup` @ `0x688` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | I2C2 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x689` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | GP_0 | Disabled (0) \| Enabled (1) | Enabled | `PchSetup` @ `0x68a` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | GP_1 | Disabled (0) \| Enabled (1) | Enabled | `PchSetup` @ `0x68b` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | GP_2 | Disabled (0) \| Enabled (1) | Enabled | `PchSetup` @ `0x68c` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | GP_3 | Disabled (0) \| Enabled (1) | Enabled | `PchSetup` @ `0x68d` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | GP_4 | Disabled (0) \| Enabled (1) | Enabled | `PchSetup` @ `0x68e` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | GP_5 | Disabled (0) \| Enabled (1) | Enabled | `PchSetup` @ `0x68f` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | GP_6 | Disabled (0) \| Enabled (1) | Enabled | `PchSetup` @ `0x690` (1) |
| Advanced > PCH-IO Configuration > ISH Configuration | GP_7 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x691` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration | PCI Express Clock Gating | Disabled (0x1) \| Enabled (0x0) | Enabled | `PchSetup` @ `0x0d0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration | DMI Link ASPM Control | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x4f6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration | Port8xh Decode | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x0d1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration | Port8xh Decode Port# | 0 … 23 (step 1) | 0 | `PchSetup` @ `0x0d2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration | Peer Memory Write Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x0d3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration | Compliance Test Mode | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x0d4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration | PCIe-USB Glitch W/A | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x0d5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration | PCIe function swap | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3c6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration | Number of Coefficients to be used for equalization | 0 … 5 (step 1) | 3 | `PchSetup` @ `0x6ea` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > IMR Configuration | PCIe IMR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3ea` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > IMR Configuration | PCIe IMR Size | 0 … 1024 (step 1) | 0 | `PchSetup` @ `0x3eb` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > IMR Configuration | RP index for IMR | 1 … 24 (step 1) | 1 | `PchSetup` @ `0x3ed` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE1  Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x336` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE1  Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x34e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE2  Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x337` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE2  Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x34f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE3  Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x338` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE3  Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x350` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE4  Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x339` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE4  Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x351` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE5  Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x33a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE5  Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x352` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE6  Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x33b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE6  Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x353` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE7  Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x33c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE7  Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x354` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE8  Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x33d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE8  Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x355` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE9  Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x33e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE9  Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x356` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE10 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x33f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE10 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x357` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE11 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x340` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE11 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x358` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE12 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x341` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE12 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x359` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE13 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x342` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE13 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x35a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE14 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x343` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE14 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x35b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE15 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x344` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE15 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x35c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE16 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x345` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE16 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x35d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE17 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x346` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE17 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x35e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE18 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x347` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE18 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x35f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE19 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x348` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE19 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x360` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE20 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x349` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE20 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x361` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE21 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x34a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE21 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x362` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE22 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x34b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE22 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x363` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE23 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x34c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE23 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x364` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE24 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x34d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | PCIE24 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x365` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | Override SW EQ settings | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3df` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | Coeff0 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x3e0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | Coeff0 Cp | 0 … 63 (step 1) | 8 | `PchSetup` @ `0x3e5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | Coeff1 Cm | 0 … 63 (step 1) | 6 | `PchSetup` @ `0x3e1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | Coeff1 Cp | 0 … 63 (step 1) | 12 | `PchSetup` @ `0x3e6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | Coeff2 Cm | 0 … 63 (step 1) | 8 | `PchSetup` @ `0x3e2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | Coeff2 Cp | 0 … 63 (step 1) | 8 | `PchSetup` @ `0x3e7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | Coeff3 Cm | 0 … 63 (step 1) | 10 | `PchSetup` @ `0x3e3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | Coeff3 Cp | 0 … 63 (step 1) | 8 | `PchSetup` @ `0x3e8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | Coeff4 Cm | 0 … 63 (step 1) | 12 | `PchSetup` @ `0x3e4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Gen3 Eq Lanes | Coeff4 Cp | 0 … 63 (step 1) | 2 | `PchSetup` @ `0x3e9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | PCI Express Root Port 1 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x0f6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3c7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x37e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | ASPM 0 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x10e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x276` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2ee` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x306` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x31e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x28e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2a6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2be` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2d6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x126` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x13e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x156` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x16e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x186` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1b6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1ce` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1e6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x1fe` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x216` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x22e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x246` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x25e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x396` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x4f7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x50f` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x53f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3ee` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x41e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x47e` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x436` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x44e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4ae` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x466` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4de` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x406` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6ad` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6c5` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x6f5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 1 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x70d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | PCI Express Root Port 10 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x0ff` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3d0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x387` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | ASPM 9 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x117` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x27f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2f7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x30f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x327` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x297` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2af` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2c7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2df` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x12f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x147` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x15f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x177` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x18f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1bf` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1d7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1ef` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x207` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x21f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x237` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x24f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x267` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3a8` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x500` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x521` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x548` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3f7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x427` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x490` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x43f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x457` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4c0` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x46f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4e7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x40f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6b6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6d7` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x6fe` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 10 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x716` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | PCI Express Root Port 11 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x100` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3d1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x388` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | ASPM 10 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x118` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x280` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2f8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x310` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x328` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x298` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2b0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2c8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2e0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x130` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x148` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x160` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x178` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x190` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1c0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1d8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1f0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x208` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x220` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x238` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x250` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x268` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3aa` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x501` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x523` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x549` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3f8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x428` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x492` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x440` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x458` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4c2` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x470` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4e8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x410` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6b7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6d9` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x6ff` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 11 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x717` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | PCI Express Root Port 12 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x101` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3d2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x389` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | ASPM 11 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x119` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x281` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2f9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x311` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x329` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x299` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2b1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2c9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2e1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x131` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x149` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x161` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x179` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x191` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1c1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1d9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1f1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x209` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x221` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x239` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x251` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x269` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3ac` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x502` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x525` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x54a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3f9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x429` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x494` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x441` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x459` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4c4` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x471` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4e9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x411` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6b8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6db` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x700` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 12 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x718` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | PCI Express Root Port 13 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x102` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3d3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x38a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | ASPM 12 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x11a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x282` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2fa` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x312` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x32a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x29a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2b2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2ca` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2e2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x132` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x14a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x162` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x17a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x192` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1c2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1da` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1f2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x20a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x222` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x23a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x252` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x26a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3ae` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x503` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x527` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x54b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3fa` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x42a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x496` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x442` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x45a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4c6` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x472` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4ea` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x412` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6b9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6dd` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x701` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 13 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x719` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | PCI Express Root Port 14 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x103` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3d4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x38b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | ASPM 13 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x11b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x283` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2fb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x313` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x32b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x29b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2b3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2cb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2e3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x133` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x14b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x163` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x17b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x193` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1c3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1db` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1f3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x20b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x223` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x23b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x253` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x26b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3b0` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x504` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x529` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x54c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3fb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x42b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x498` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x443` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x45b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4c8` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x473` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4eb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x413` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6ba` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6df` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x702` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 14 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x71a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | PCI Express Root Port 15 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x104` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3d5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x38c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | ASPM 14 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | L1 | `PchSetup` @ `0x11c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | Disabled | `PchSetup` @ `0x284` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2fc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x314` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x32c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x29c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2b4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2cc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2e4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x134` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x14c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x164` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x17c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x194` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1c4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1dc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1f4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x20c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x224` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x23c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x254` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x26c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3b2` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x505` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x52b` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x54d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3fc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x42c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x49a` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x444` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x45c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4ca` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x474` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4ec` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x414` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6bb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6e1` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x703` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 15 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x71b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | PCI Express Root Port 16 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x105` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3d6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x38d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | ASPM 15 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x11d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x285` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2fd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x315` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x32d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x29d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2b5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2cd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2e5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x135` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x14d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x165` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x17d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x195` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1c5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1dd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1f5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x20d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x225` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x23d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x255` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x26d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3b4` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x506` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x52d` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x54e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3fd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x42d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x49c` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x445` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x45d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4cc` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x475` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4ed` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x415` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6bc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6e3` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x704` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 16 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x71c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | PCI Express Root Port 17 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x106` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3d7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x38e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | ASPM 16 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x11e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x286` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2fe` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x316` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x32e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x29e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2b6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2ce` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2e6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x136` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x14e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x166` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x17e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x196` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1c6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1de` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1f6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x20e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x226` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x23e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x256` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x26e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3b6` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x507` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x52f` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x54f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3fe` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x42e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x49e` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x446` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x45e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4ce` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x476` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4ee` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x416` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6bd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6e5` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x705` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 17 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x71d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | PCI Express Root Port 18 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x107` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3d8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x38f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | ASPM 17 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x11f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x287` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2ff` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x317` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x32f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x29f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2b7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2cf` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2e7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x137` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x14f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x167` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x17f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x197` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1c7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1df` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1f7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x20f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x227` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x23f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x257` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x26f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3b8` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x508` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x531` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x550` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3ff` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x42f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4a0` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x447` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x45f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4d0` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x477` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4ef` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x417` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6be` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6e7` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x706` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 18 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x71e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | PCI Express Root Port 19 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x108` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3d9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x390` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | ASPM 18 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x120` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x288` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x300` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x318` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x330` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2a0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2b8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2d0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2e8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x138` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x150` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x168` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x180` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x198` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1c8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1e0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1f8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x210` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x228` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x240` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x258` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x270` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3ba` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x509` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x533` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x551` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x400` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x430` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4a2` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x448` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x460` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4d2` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x478` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4f0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x418` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6bf` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6e9` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x707` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 19 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x71f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | PCI Express Root Port 2 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x0f7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3c8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x37f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | ASPM 1 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x10f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x277` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2ef` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x307` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x31f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x28f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2a7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2bf` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2d7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x127` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x13f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x157` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x16f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x187` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1b7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1cf` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1e7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x1ff` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x217` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x22f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x247` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x25f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x398` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x4f8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x511` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x540` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3ef` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x41f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x480` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x437` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x44f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4b0` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x467` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4df` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x407` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6ae` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6c7` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x6f6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 2 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x70e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | PCI Express Root Port 20 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x109` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3da` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x391` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | ASPM 19 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x121` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x289` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x301` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x319` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x331` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2a1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2b9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2d1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2e9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x139` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x151` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x169` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x181` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x199` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1c9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1e1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1f9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x211` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x229` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x241` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x259` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x271` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3bc` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x50a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x535` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x552` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x401` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x431` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4a4` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x449` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x461` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4d4` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x479` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4f1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x419` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6c0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6eb` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x708` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 20 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x720` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | PCI Express Root Port 21 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x10a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3db` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x392` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | ASPM 20 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | L1 | `PchSetup` @ `0x122` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | Disabled | `PchSetup` @ `0x28a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x302` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x31a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x332` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2a2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2ba` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2d2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2ea` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x13a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x152` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x16a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x182` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x19a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1ca` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1e2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1fa` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x212` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x22a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x242` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x25a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x272` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3be` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x50b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x537` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x553` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x402` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x432` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4a6` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x44a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x462` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4d6` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x47a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4f2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x41a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6c1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6ed` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x709` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 21 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x721` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | PCI Express Root Port 22 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x10b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3dc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x393` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | ASPM 21 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x123` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x28b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x303` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x31b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x333` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2a3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2bb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2d3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2eb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x13b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x153` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x16b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x183` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x19b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1cb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1e3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1fb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x213` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x22b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x243` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x25b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x273` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3c0` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x50c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x539` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x554` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x403` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x433` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4a8` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x44b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x463` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4d8` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x47b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4f3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x41b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6c2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6ef` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x70a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 22 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x722` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | PCI Express Root Port 23 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x10c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3dd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x394` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | ASPM 22 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x124` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x28c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x304` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x31c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x334` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2a4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2bc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2d4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2ec` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x13c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x154` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x16c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x184` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x19c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1cc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1e4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1fc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x214` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x22c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x244` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x25c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x274` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3c2` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x50d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x53b` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x555` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x404` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x434` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4aa` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x44c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x464` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4da` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x47c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4f4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x41c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6c3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6f1` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x70b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 23 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x723` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | PCI Express Root Port 24 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x10d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3de` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x395` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | ASPM 23 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x125` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x28d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x305` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x31d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x335` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2a5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2bd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2d5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2ed` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x13d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x155` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x16d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x185` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x19d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1cd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1e5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1fd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x215` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x22d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x245` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x25d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x275` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3c4` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x50e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x53d` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x556` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x405` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x435` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4ac` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x44d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x465` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4dc` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x47d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4f5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x41d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6c4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6f3` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x70c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 24 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x724` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | PCI Express Root Port 3 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x0f8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3c9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x380` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | ASPM 2 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x110` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x278` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2f0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x308` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x320` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x290` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2a8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2c0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2d8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x128` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x140` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x158` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x170` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x188` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1b8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1d0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1e8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x200` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x218` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x230` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x248` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x260` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x39a` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x4f9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x513` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x541` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3f0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x420` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x482` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x438` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x450` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4b2` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x468` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4e0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x408` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6af` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6c9` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x6f7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 3 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x70f` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | PCI Express Root Port 4 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x0f9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3ca` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x381` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | ASPM 3 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x111` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x279` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2f1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x309` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x321` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x291` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2a9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2c1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2d9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x129` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x141` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x159` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x171` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x189` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1b9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1d1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1e9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x201` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x219` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x231` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x249` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x261` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x39c` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x4fa` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x515` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x542` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3f1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x421` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x484` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x439` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x451` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4b4` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x469` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4e1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x409` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6b0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6cb` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x6f8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 4 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x710` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | PCI Express Root Port 5 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x0fa` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3cb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x382` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | ASPM 4 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x112` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x27a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2f2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x30a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x322` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x292` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2aa` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2c2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2da` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x12a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x142` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x15a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x172` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x18a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1ba` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1d2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1ea` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x202` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x21a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x232` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x24a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x262` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x39e` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x4fb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x517` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x543` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3f2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x422` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x486` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x43a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x452` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4b6` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x46a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4e2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x40a` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6b1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6cd` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x6f9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 5 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x711` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | PCI Express Root Port 6 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x0fb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3cc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x383` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | ASPM 5 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x113` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x27b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2f3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x30b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x323` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x293` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2ab` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2c3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2db` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x12b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x143` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x15b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x173` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x18b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1bb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1d3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1eb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x203` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x21b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x233` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x24b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x263` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3a0` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x4fc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x519` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x544` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3f3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x423` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x488` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x43b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x453` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4b8` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x46b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4e3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x40b` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6b2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6cf` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x6fa` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 6 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x712` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | PCI Express Root Port 7 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x0fc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3cd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x384` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | ASPM 6 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x114` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x27c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2f4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x30c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x324` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x294` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2ac` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2c4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2dc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x12c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x144` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x15c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x174` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x18c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1bc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1d4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1ec` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x204` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x21c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x234` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x24c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x264` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3a2` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x4fd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x51b` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x545` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3f4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x424` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x48a` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x43c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x454` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4ba` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x46c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4e4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x40c` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6b3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6d1` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x6fb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 7 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x713` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | PCI Express Root Port 8 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x0fd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3ce` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x385` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | ASPM 7 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | Auto | `PchSetup` @ `0x115` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | L1.1 & L1.2 | `PchSetup` @ `0x27d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2f5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x30d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x325` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x295` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2ad` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2c5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2dd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x12d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x145` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x15d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x175` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x18d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1bd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1d5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1ed` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x205` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x21d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x235` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x24d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x265` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3a4` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x4fe` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x51d` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x546` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3f5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x425` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x48c` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x43d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x455` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4bc` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x46d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4e5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x40d` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6b4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6d3` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x6fc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 8 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x714` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | PCI Express Root Port 9 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x0fe` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Disable Gen2 Pll Shutdown and L1 Controller Power gating | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x3cf` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Connection Type | Built-in (0x0) \| Slot (0x1) | Slot | `PchSetup` @ `0x386` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | ASPM 8 | Disabled (0x0) \| L0s (0x1) \| L1 (0x2) \| L0sL1 (0x3) \| Auto (0x4) | L1 | `PchSetup` @ `0x116` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | L1 Substates | Disabled (0x0) \| L1.1 (0x1) \| L1.1 & L1.2 (0x2) | Disabled | `PchSetup` @ `0x27e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Gen3 Eq Phase3 Method | Hardware (0x1) \| Static Coeff. (0x4) | Hardware | `PchSetup` @ `0x2f6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | UPTP | 0 … 10 (step 1) | 5 | `PchSetup` @ `0x30e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | DPTP | 0 … 10 (step 1) | 7 | `PchSetup` @ `0x326` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | ACS | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x296` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | PTM | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2ae` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | DPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2c6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | EDPC | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x2de` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | URR | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x12e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | FER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x146` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | NFER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x15e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | CER | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x176` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | CTO | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x18e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | SEFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1be` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | SENFE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1d6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | SECE | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x1ee` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | PME SCI | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x206` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x21e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Advanced Error Reporting | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x236` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | PCIe Speed | Auto (0x0) \| Gen1 (0x1) \| Gen2 (0x2) \| Gen3 (0x3) | Auto | `PchSetup` @ `0x24e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Transmitter Half Swing | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x266` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Detect Timeout | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x3a6` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Extra Bus Reserved | 0 … 7 (step 1) | 0 | `PchSetup` @ `0x4ff` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Reserved Memory | 1 … 20 (step 1) | 10 | `PchSetup` @ `0x51f` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Reserved I/O | 4 … 20 (step 4) | 4 | `PchSetup` @ `0x547` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | LTR | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x3f6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x426` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x48e` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x43e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Non Snoop Latency Override | Disabled (0x0) \| Manual (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x456` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Non Snoop Latency Value | 0 … 1023 (step 1) | 60 | `PchSetup` @ `0x4be` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Non Snoop Latency Multiplier | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `PchSetup` @ `0x46e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | Force LTR Override | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x4e6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 | LTR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x40e` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 > Extra options | Detect Non-Compliance Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `Setup` @ `0x6b5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 > Extra options | Prefetchable Memory | 1 … 20 (step 1) | 10 | `Setup` @ `0x6d5` (2) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 > Extra options | Reserved Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x6fd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCI Express Root Port 9 > Extra options | Prefetchable Memory Alignment | 1 … 31 (step 1) | 1 | `Setup` @ `0x715` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock0 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Enabled | `PchSetup` @ `0x0d6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock0 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0e6` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock1 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Disabled | `PchSetup` @ `0x0d7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock1 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0e7` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock2 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Disabled | `PchSetup` @ `0x0d8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock2 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0e8` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock3 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Disabled | `PchSetup` @ `0x0d9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock3 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0e9` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock4 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Disabled | `PchSetup` @ `0x0da` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock4 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0ea` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock5 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Disabled | `PchSetup` @ `0x0db` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock5 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0eb` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock6 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Enabled | `PchSetup` @ `0x0dc` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock6 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0ec` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock7 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Enabled | `PchSetup` @ `0x0dd` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock7 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0ed` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock8 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Disabled | `PchSetup` @ `0x0de` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock8 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0ee` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock9 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Enabled | `PchSetup` @ `0x0df` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock9 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0ef` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock10 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Disabled | `PchSetup` @ `0x0e0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock10 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0f0` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock11 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Disabled | `PchSetup` @ `0x0e1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock11 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0f1` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock12 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Enabled | `PchSetup` @ `0x0e2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock12 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0f2` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock13 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Disabled | `PchSetup` @ `0x0e3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock13 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0f3` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock14 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Enabled | `PchSetup` @ `0x0e4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock14 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0f4` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | Clock15 assignment | Platform-POR (0x0) \| Enabled (0x1) \| Disabled (0x2) | Enabled | `PchSetup` @ `0x0e5` (1) |
| Advanced > PCH-IO Configuration > PCI Express Configuration > PCIE clocks | ClkReq for Clock15 | Platform-POR (0x0) \| Disabled (0xff) | Platform-POR | `PchSetup` @ `0x0f5` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Thermal Throttling Level | Suggested Setting (0x1) \| Manual (0x0) | Suggested Setting | `PchSetup` @ `0x6ba` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Thermal Throttling | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x6c1` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | TT State 13 | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x6c2` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Thermal Throttling Lock | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x6c3` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | T0 Level | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x6bb` (2) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | T1 Level | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x6bd` (2) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | T2 Level | 0 … 65535 (step 1) | 0 | `PchSetup` @ `0x6bf` (2) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | DMI Thermal Setting | Suggested Setting (0x1) \| Manual (0x0) | Suggested Setting | `PchSetup` @ `0x6c4` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | DMI Thermal Sensor Autonomous Width | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x6c9` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Thermal Sensor 0 Width | x1 (0x0) \| x2 (0x1) \| x4 (0x2) \| x8 (0x3) \| x16 (0x4) | x8 | `PchSetup` @ `0x6c5` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Thermal Sensor 1 Width | x1 (0x0) \| x2 (0x1) \| x4 (0x2) \| x8 (0x3) \| x16 (0x4) | x4 | `PchSetup` @ `0x6c6` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Thermal Sensor 2 Width | x1 (0x0) \| x2 (0x1) \| x4 (0x2) \| x8 (0x3) \| x16 (0x4) | x2 | `PchSetup` @ `0x6c7` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Thermal Sensor 3 Width | x1 (0x0) \| x2 (0x1) \| x4 (0x2) \| x8 (0x3) \| x16 (0x4) | x1 | `PchSetup` @ `0x6c8` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | SATA Thermal Setting | Suggested Setting (0x1) \| Manual (0x0) | Suggested Setting | `PchSetup` @ `0x6ca` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | T1 Multipler | Disabled (0x0) \| x1 (0x1) \| x2 (0x2) \| x4 (0x3) | x1 | `PchSetup` @ `0x6cb` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | T2 Multipler | Disabled (0x0) \| x1 (0x1) \| x2 (0x2) \| x4 (0x3) | x2 | `PchSetup` @ `0x6cc` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | T3 Multipler | Disabled (0x0) \| x1 (0x1) \| x2 (0x2) \| x4 (0x3) | x4 | `PchSetup` @ `0x6cd` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Alternate Fast Init Tdispatch | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x6d0` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Tdispatch | ~32us (0x0) \| ~128us (0x1) \| ~8us (0x3) | 90 | `PchSetup` @ `0x6ce` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Tinactive | ~32us (0x0) \| ~128us (0x1) \| ~8us (0x3) | 90 | `PchSetup` @ `0x6cf` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Tdispatch | ~32ms (0x0) \| ~128ms (0x1) \| ~8ms (0x3) | 90 | `PchSetup` @ `0x6ce` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Tinactive | ~32ms (0x0) \| ~128ms (0x1) \| ~8ms (0x3) | 90 | `PchSetup` @ `0x6cf` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | T1 Multipler | Disabled (0x0) \| x1 (0x1) \| x2 (0x2) \| x4 (0x3) | x1 | `PchSetup` @ `0x6d1` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | T2 Multipler | Disabled (0x0) \| x1 (0x1) \| x2 (0x2) \| x4 (0x3) | x2 | `PchSetup` @ `0x6d2` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | T3 Multipler | Disabled (0x0) \| x1 (0x1) \| x2 (0x2) \| x4 (0x3) | x4 | `PchSetup` @ `0x6d3` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Alternate Fast Init Tdispatch | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x6d6` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Tdispatch | ~32us (0x0) \| ~128us (0x1) \| ~8us (0x3) \| ~32ms (0x0) \| ~128ms (0x1) \| ~8ms (0x3) | 90 | `PchSetup` @ `0x6d4` (1) |
| Advanced > PCH-IO Configuration > Pch Thermal Throttling Control | Tinactive | ~32us (0x0) \| ~128us (0x1) \| ~8us (0x3) \| ~32ms (0x0) \| ~128ms (0x1) \| ~8ms (0x3) | 90 | `PchSetup` @ `0x6d5` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Controller(s) | Enabled (0x1) \| Disabled (0x0) | 1 | `PchSetup` @ `0x043` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Mode Selection | AHCI (0x0) \| RAID (0x1) | AHCI | `PchSetup` @ `0x044` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Sata Interrupt Selection | Msix (0x0) \| Msi (0x1) \| Legacy (0x2) | Msix | `PchSetup` @ `0x045` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 1 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0b8` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 2 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0b9` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 3 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0ba` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 4 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0bb` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 5 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0bc` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 6 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0bd` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 7 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0be` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 8 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0bf` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 9 | RST Controlled (0x1) \| Not RST Controlled (0x0) | RST Controlled | `PchSetup` @ `0x0c0` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 10 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0c1` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 11 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0c2` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 12 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0c3` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 13 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0c4` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 14 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0c5` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 15 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0c6` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 16 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0c7` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 17 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0c8` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 18 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0c9` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 19 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0ca` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 20 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0cb` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 21 | RST Controlled (0x1) \| Not RST Controlled (0x0) | RST Controlled | `PchSetup` @ `0x0cc` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 22 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0cd` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 23 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0ce` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | PCIe Storage Dev On Port 24 | RST Controlled (0x1) \| Not RST Controlled (0x0) | Not RST Controlled | `PchSetup` @ `0x0cf` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Test Mode | Enabled (0x1) \| Disabled (0x0) | Disabled | `PchSetup` @ `0x08f` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | RAID Device ID | Client (0x0) \| Alternate (0x1) \| Server (0x2) | Client | `PchSetup` @ `0x08d` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Aggressive LPM Support | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x08e` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Port 0 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x046` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x04e` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | External | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x066` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Mechanical Presence Switch | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x056` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Spin Up Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x05e` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Device Type | Hard Disk Drive (0x0) \| Solid State Drive (0x1) | Hard Disk Drive | `PchSetup` @ `0x06e` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Port 0 DevSlp | Disabled (0x0) \| Enabled (0x1) | 0 | `PchSetup` @ `0x090` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Configuration | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x098` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Value | 0 … 1023 (step 0) | 625 | `PchSetup` @ `0x0a0` (2) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DM Value | 0 … 15 (step 0) | 15 | `PchSetup` @ `0x0b0` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Port 1 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x047` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x04f` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | External | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x067` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Mechanical Presence Switch | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x057` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Spin Up Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x05f` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Device Type | Hard Disk Drive (0x0) \| Solid State Drive (0x1) | Hard Disk Drive | `PchSetup` @ `0x06f` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Port 1 DevSlp | Disabled (0x0) \| Enabled (0x1) | 0 | `PchSetup` @ `0x091` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Configuration | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x099` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Value | 0 … 1023 (step 0) | 625 | `PchSetup` @ `0x0a2` (2) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DM Value | 0 … 15 (step 0) | 15 | `PchSetup` @ `0x0b1` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Port 2 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x048` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x050` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | External | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x068` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Mechanical Presence Switch | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x058` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Spin Up Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x060` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Device Type | Hard Disk Drive (0x0) \| Solid State Drive (0x1) | Hard Disk Drive | `PchSetup` @ `0x070` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Port 2 DevSlp | Disabled (0x0) \| Enabled (0x1) | 0 | `PchSetup` @ `0x092` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Configuration | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x09a` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Value | 0 … 1023 (step 0) | 90 | `PchSetup` @ `0x0a4` (2) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DM Value | 0 … 15 (step 0) | 15 | `PchSetup` @ `0x0b2` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Port 3 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x049` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x051` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | External | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x069` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Mechanical Presence Switch | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x059` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Spin Up Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x061` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Device Type | Hard Disk Drive (0x0) \| Solid State Drive (0x1) | Hard Disk Drive | `PchSetup` @ `0x071` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Port 3 DevSlp | Disabled (0x0) \| Enabled (0x1) | 0 | `PchSetup` @ `0x093` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Configuration | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x09b` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Value | 0 … 1023 (step 0) | 625 | `PchSetup` @ `0x0a6` (2) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DM Value | 0 … 15 (step 0) | 15 | `PchSetup` @ `0x0b3` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Port 4 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x04a` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x052` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | External | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x06a` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Mechanical Presence Switch | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x05a` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Spin Up Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x062` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Device Type | Hard Disk Drive (0x0) \| Solid State Drive (0x1) | Hard Disk Drive | `PchSetup` @ `0x072` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Port 4 DevSlp | Disabled (0x0) \| Enabled (0x1) | 0 | `PchSetup` @ `0x094` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Configuration | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x09c` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Value | 0 … 1023 (step 0) | 625 | `PchSetup` @ `0x0a8` (2) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DM Value | 0 … 15 (step 0) | 15 | `PchSetup` @ `0x0b4` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Port 5 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x04b` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x053` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | External | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x06b` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Mechanical Presence Switch | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x05b` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Spin Up Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x063` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Device Type | Hard Disk Drive (0x0) \| Solid State Drive (0x1) | Hard Disk Drive | `PchSetup` @ `0x073` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Port 5 DevSlp | Disabled (0x0) \| Enabled (0x1) | 0 | `PchSetup` @ `0x095` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Configuration | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x09d` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Value | 0 … 1023 (step 0) | 625 | `PchSetup` @ `0x0aa` (2) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DM Value | 0 … 15 (step 0) | 15 | `PchSetup` @ `0x0b5` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Port 6 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x04c` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x054` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | External | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x06c` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Mechanical Presence Switch | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x05c` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Spin Up Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x064` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Device Type | Hard Disk Drive (0x0) \| Solid State Drive (0x1) | Hard Disk Drive | `PchSetup` @ `0x074` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Port 6 DevSlp | Disabled (0x0) \| Enabled (0x1) | 0 | `PchSetup` @ `0x096` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Configuration | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x09e` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Value | 0 … 1023 (step 0) | 625 | `PchSetup` @ `0x0ac` (2) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DM Value | 0 … 15 (step 0) | 15 | `PchSetup` @ `0x0b6` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Port 7 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x04d` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Hot Plug | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x055` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | External | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x06d` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Mechanical Presence Switch | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x05d` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | Spin Up Device | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x065` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Device Type | Hard Disk Drive (0x0) \| Solid State Drive (0x1) | Hard Disk Drive | `PchSetup` @ `0x075` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | SATA Port 7 DevSlp | Disabled (0x0) \| Enabled (0x1) | 0 | `PchSetup` @ `0x097` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Configuration | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x09f` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DITO Value | 0 … 1023 (step 0) | 625 | `PchSetup` @ `0x0ae` (2) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration | DM Value | 0 … 15 (step 0) | 15 | `PchSetup` @ `0x0b7` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | HDD Unlock | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x084` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | LED Locate | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x085` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | Use RST Legacy OROM | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x08a` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | RAID0 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x07e` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | RAID1 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x07f` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | RAID10 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x080` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | RAID5 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x081` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | Intel Rapid Recovery Technology | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x082` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | OROM UI and BANNER | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x083` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | IRRT Only on eSATA | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x086` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | Smart Response Technology | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x087` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | OROM UI Normal Delay | 2 secs (0x0) \| 4 secs (0x1) \| 6 secs (0x2) \| 8 secs (0x3) | 2 secs | `PchSetup` @ `0x088` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | RST Force Form | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x089` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | System Acceleration with Intel(R) Optane(TM) Memory | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x08b` (1) |
| Advanced > PCH-IO Configuration > SATA And RST Configuration > Software Feature Mask Configuration | CPU Attached Storage | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x08c` (1) |
| Advanced > PCH-IO Configuration > SCS Configuration | eMMC 5.0 Controller | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x67e` (1) |
| Advanced > PCH-IO Configuration > SCS Configuration | Driver Strength | 33 Ohm (0x0) \| 40 Ohm (0x1) \| 50 Ohm (0x2) | 50 Ohm | `PchSetup` @ `0x680` (1) |
| Advanced > PCH-IO Configuration > SCS Configuration | eMMC 5.0 HS400 Mode | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x67f` (1) |
| Advanced > PCH-IO Configuration > SCS Configuration | Enable HS400 software tuning | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x6eb` (1) |
| Advanced > PCH-IO Configuration > SCS Configuration | SDCard 3.0 Controller | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x681` (1) |
| Advanced > PCH-IO Configuration > SCS Configuration | UFS 2.0 Controller | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x682` (1) |
| Advanced > PCH-IO Configuration > Security Configuration | RTC Memory Lock | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x016` (1) |
| Advanced > PCH-IO Configuration > Security Configuration | BIOS Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x017` (1) |
| Advanced > PCH-IO Configuration > Security Configuration | Force unlock on all GPIO pads | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x018` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | I2C0 Controller | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x6a8` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | I2C1 Controller | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x6a9` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | I2C2 Controller | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x6aa` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | I2C3 Controller | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x6ab` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | I2C4 Controller | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x6ac` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | I2C5 Controller | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x6ad` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | SPI0 Controller | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x699` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | SPI1 Controller | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x69a` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | SPI2 Controller | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x69b` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | UART0 Controller | Disabled (0x0) \| Enabled (0x1) \| Communication port (COM) (0x3) | Disabled | `PchSetup` @ `0x69c` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | UART1 Controller | Disabled (0x0) \| Enabled (0x1) \| Communication port (COM) (0x3) | Disabled | `PchSetup` @ `0x69d` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | UART2 Controller | Disabled (0x0) \| Communication port (COM) (0x3) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x69e` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | GPIO IRQ Route | IRQ14 (0xe) \| IRQ15 (0xf) | IRQ14 | `PchSetup` @ `0x6b2` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | WITT/MITT Test Device | Disabled (0x0) \| Enabled - I2C0 (0x1) \| Enabled - I2C1 (0x2) \| Enabled - I2C2 (0x3) \| Enabled - I2C3 (0x4) \| Enabled - I2C4 (0x5) \| E… | Disabled | `Setup` @ `0x2c9` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | WITT/MITT Device selection | WITT (0x0) \| MITT (0x1) | MITT | `Setup` @ `0x2ca` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | UART Test Device | Disabled (0x0) \| Enabled - UART0 (0x1) \| Enabled - UART1 (0x2) \| Enabled - UART2 (0x3) | Disabled | `Setup` @ `0x2cb` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | Additional Serial IO devices | Disabled (0) \| Enabled (1) | Disabled | `PchSetup` @ `0x6b6` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration | SerialIO timing parameters | Disabled (0) \| Enabled (1) | 1 | `Setup` @ `0x2ce` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | StandardSpeed SCL High | 0 … 65535 (step 0) | 1010 | `Setup` @ `0x2cf` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | StandardSpeed SCL Low | 0 … 65535 (step 0) | 1085 | `Setup` @ `0x2d1` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | StandardSpeed SDA Hold | 0 … 65535 (step 0) | 28 | `Setup` @ `0x2d3` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | FastSpeed SCL High | 0 … 65535 (step 0) | 193 | `Setup` @ `0x2d5` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | FastSpeed SCL Low | 0 … 65535 (step 0) | 313 | `Setup` @ `0x2d7` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | FastSpeed SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x2d9` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | FastSpeedPlus SCL High | 0 … 65535 (step 0) | 61 | `Setup` @ `0x2db` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | FastSpeedPlus SCL Low | 0 … 65535 (step 0) | 132 | `Setup` @ `0x2dd` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | FastSpeedPlus SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x2df` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | HighSpeed SCL High | 0 … 65535 (step 0) | 11 | `Setup` @ `0x2e1` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | HighSpeed SCL Low | 0 … 65535 (step 0) | 19 | `Setup` @ `0x2e3` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | HighSpeed SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x2e5` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | D0->D3 idle timeout (screen off) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x35f` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings | D0->D3 idle timeout (screen on) | 1 … 10000 (step 0) | 2000 | `Setup` @ `0x361` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings > Serial IO Touch Pad Settings | Touch Pad | Disabled (0x0) \| Synaptics Precision Touchpad (0x1) \| Synaptics Forcepad (0x2) \| ALPS Precision Touchpad ClickPad (0x6) \| Custom device… | Custom device | `Setup` @ `0x2ad` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings > Serial IO Touch Pad Settings | Touch Pad Interrupt Mode | GPIO Interrupt (0x0) \| APIC Interrupt (0x1) | GPIO Interrupt | `Setup` @ `0x2ae` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings > Serial IO Touch Pad Settings | Device's bus address | 0 … 127 (step 1) | 44 | `Setup` @ `0x2af` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings > Serial IO Touch Pad Settings | Device's HID address | 0 … 65535 (step 1) | 32 | `Setup` @ `0x2b0` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings > Serial IO Touch Pad Settings | Device's bus speed | 100kHz (0x0) \| 400kHz (0x1) \| 1MHz (0x2) | 400kHz | `Setup` @ `0x2b2` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings > Serial IO Touch Panel Settings | Touch Panel | Disabled (0x0) \| Atmel3432 TouchPanel (0x1) \| Atmel2952 TouchPanel (0x2) \| Elan2097 TouchPanel (0x3) \| N-Trig/Samsung 13.3" (0x4) \| N-… | Disabled | `Setup` @ `0x2b3` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings > Serial IO Touch Panel Settings | Touch Panel Interrupt Mode | GPIO Interrupt (0x0) \| APIC Interrupt (0x1) | APIC Interrupt | `Setup` @ `0x2b4` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings > Serial IO Touch Panel Settings | Device's bus address | 0 … 127 (step 1) | 0 | `Setup` @ `0x2b5` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings > Serial IO Touch Panel Settings | Device's HID address | 0 … 65535 (step 1) | 0 | `Setup` @ `0x2b6` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C0 Settings > Serial IO Touch Panel Settings | Device's bus speed | 100kHz (0x0) \| 400kHz (0x1) \| 1MHz (0x2) | 400kHz | `Setup` @ `0x2b8` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | StandardSpeed SCL High | 0 … 65535 (step 0) | 1010 | `Setup` @ `0x2e7` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | StandardSpeed SCL Low | 0 … 65535 (step 0) | 1085 | `Setup` @ `0x2e9` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | StandardSpeed SDA Hold | 0 … 65535 (step 0) | 28 | `Setup` @ `0x2eb` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | FastSpeed SCL High | 0 … 65535 (step 0) | 193 | `Setup` @ `0x2ed` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | FastSpeed SCL Low | 0 … 65535 (step 0) | 313 | `Setup` @ `0x2ef` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | FastSpeed SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x2f1` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | FastSpeedPlus SCL High | 0 … 65535 (step 0) | 61 | `Setup` @ `0x2f3` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | FastSpeedPlus SCL Low | 0 … 65535 (step 0) | 132 | `Setup` @ `0x2f5` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | FastSpeedPlus SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x2f7` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | HighSpeed SCL High | 0 … 65535 (step 0) | 11 | `Setup` @ `0x2f9` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | HighSpeed SCL Low | 0 … 65535 (step 0) | 19 | `Setup` @ `0x2fb` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | HighSpeed SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x2fd` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | D0->D3 idle timeout (screen off) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x363` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C1 Settings | D0->D3 idle timeout (screen on) | 1 … 10000 (step 0) | 2000 | `Setup` @ `0x365` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | StandardSpeed SCL High | 0 … 65535 (step 0) | 1010 | `Setup` @ `0x2ff` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | StandardSpeed SCL Low | 0 … 65535 (step 0) | 1085 | `Setup` @ `0x301` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | StandardSpeed SDA Hold | 0 … 65535 (step 0) | 28 | `Setup` @ `0x303` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | FastSpeed SCL High | 0 … 65535 (step 0) | 193 | `Setup` @ `0x305` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | FastSpeed SCL Low | 0 … 65535 (step 0) | 313 | `Setup` @ `0x307` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | FastSpeed SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x309` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | FastSpeedPlus SCL High | 0 … 65535 (step 0) | 61 | `Setup` @ `0x30b` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | FastSpeedPlus SCL Low | 0 … 65535 (step 0) | 132 | `Setup` @ `0x30d` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | FastSpeedPlus SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x30f` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | HighSpeed SCL High | 0 … 65535 (step 0) | 11 | `Setup` @ `0x311` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | HighSpeed SCL Low | 0 … 65535 (step 0) | 19 | `Setup` @ `0x313` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | HighSpeed SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x315` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | D0->D3 idle timeout (screen off) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x367` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C2 Settings | D0->D3 idle timeout (screen on) | 1 … 10000 (step 0) | 2000 | `Setup` @ `0x369` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | StandardSpeed SCL High | 0 … 65535 (step 0) | 1010 | `Setup` @ `0x317` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | StandardSpeed SCL Low | 0 … 65535 (step 0) | 1085 | `Setup` @ `0x319` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | StandardSpeed SDA Hold | 0 … 65535 (step 0) | 28 | `Setup` @ `0x31b` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | FastSpeed SCL High | 0 … 65535 (step 0) | 193 | `Setup` @ `0x31d` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | FastSpeed SCL Low | 0 … 65535 (step 0) | 313 | `Setup` @ `0x31f` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | FastSpeed SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x321` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | FastSpeedPlus SCL High | 0 … 65535 (step 0) | 61 | `Setup` @ `0x323` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | FastSpeedPlus SCL Low | 0 … 65535 (step 0) | 132 | `Setup` @ `0x325` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | FastSpeedPlus SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x327` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | HighSpeed SCL High | 0 … 65535 (step 0) | 11 | `Setup` @ `0x329` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | HighSpeed SCL Low | 0 … 65535 (step 0) | 19 | `Setup` @ `0x32b` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | HighSpeed SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x32d` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | D0->D3 idle timeout (screen off) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x36b` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C3 Settings | D0->D3 idle timeout (screen on) | 1 … 10000 (step 0) | 2000 | `Setup` @ `0x36d` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | StandardSpeed SCL High | 0 … 65535 (step 0) | 1010 | `Setup` @ `0x32f` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | StandardSpeed SCL Low | 0 … 65535 (step 0) | 1085 | `Setup` @ `0x331` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | StandardSpeed SDA Hold | 0 … 65535 (step 0) | 28 | `Setup` @ `0x333` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | FastSpeed SCL High | 0 … 65535 (step 0) | 193 | `Setup` @ `0x335` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | FastSpeed SCL Low | 0 … 65535 (step 0) | 313 | `Setup` @ `0x337` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | FastSpeed SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x339` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | FastSpeedPlus SCL High | 0 … 65535 (step 0) | 61 | `Setup` @ `0x33b` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | FastSpeedPlus SCL Low | 0 … 65535 (step 0) | 132 | `Setup` @ `0x33d` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | FastSpeedPlus SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x33f` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | HighSpeed SCL High | 0 … 65535 (step 0) | 11 | `Setup` @ `0x341` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | HighSpeed SCL Low | 0 … 65535 (step 0) | 19 | `Setup` @ `0x343` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | HighSpeed SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x345` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | D0->D3 idle timeout (screen off) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x36f` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C4 Settings | D0->D3 idle timeout (screen on) | 1 … 10000 (step 0) | 2000 | `Setup` @ `0x371` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | StandardSpeed SCL High | 0 … 65535 (step 0) | 1010 | `Setup` @ `0x347` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | StandardSpeed SCL Low | 0 … 65535 (step 0) | 1085 | `Setup` @ `0x349` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | StandardSpeed SDA Hold | 0 … 65535 (step 0) | 28 | `Setup` @ `0x34b` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | FastSpeed SCL High | 0 … 65535 (step 0) | 193 | `Setup` @ `0x34d` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | FastSpeed SCL Low | 0 … 65535 (step 0) | 313 | `Setup` @ `0x34f` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | FastSpeed SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x351` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | FastSpeedPlus SCL High | 0 … 65535 (step 0) | 61 | `Setup` @ `0x353` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | FastSpeedPlus SCL Low | 0 … 65535 (step 0) | 132 | `Setup` @ `0x355` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | FastSpeedPlus SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x357` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | HighSpeed SCL High | 0 … 65535 (step 0) | 11 | `Setup` @ `0x359` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | HighSpeed SCL Low | 0 … 65535 (step 0) | 19 | `Setup` @ `0x35b` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | HighSpeed SDA Hold | 0 … 65535 (step 0) | 30 | `Setup` @ `0x35d` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | D0->D3 idle timeout (screen off) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x373` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO I2C5 Settings | D0->D3 idle timeout (screen on) | 1 … 10000 (step 0) | 2000 | `Setup` @ `0x375` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO SPI0 Settings | ChipSelect 0 polarity | Active Low (0x0) \| Active High (0x1) | Active High | `PchSetup` @ `0x693` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO SPI0 Settings | D0->D3 idle timeout (screen off) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x377` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO SPI0 Settings | D0->D3 idle timeout (screen on) | 1 … 10000 (step 0) | 2000 | `Setup` @ `0x379` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO SPI1 Settings | ChipSelect 0 polarity | Active Low (0x0) \| Active High (0x1) | Active High | `PchSetup` @ `0x695` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO SPI1 Settings > Serial IO Finger Print Settings | Finger Print Sensor | Disabled (0x0) \| FPC1011 (0x1) \| FPC1020 (0x2) \| VFSI6101 (0x3) \| Synaptics VFSI7500 (0x4) \| EGIS0300 (0x5) \| FPC1021 (0x6) | 0 | `Setup` @ `0x2c5` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO SPI1 Settings > Serial IO Finger Print Settings | Finger Print Interrupt Mode | GPIO Interrupt (0x0) \| APIC Interrupt (0x1) | APIC Interrupt | `Setup` @ `0x2c6` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO SPI1 Settings > Serial IO Finger Print Settings | D0->D3 idle timeout (screen off) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x37b` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO SPI1 Settings > Serial IO Finger Print Settings | D0->D3 idle timeout (screen on) | 1 … 10000 (step 0) | 2000 | `Setup` @ `0x37d` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO SPI1 Settings > Serial IO Finger Print Settings | D0->D3 idle timeout (screen off) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x37f` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO SPI1 Settings > Serial IO Finger Print Settings | D0->D3 idle timeout (screen on) | 1 … 10000 (step 0) | 2000 | `Setup` @ `0x381` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO SPI2 Settings | ChipSelect 0 polarity | Active Low (0x0) \| Active High (0x1) | Active High | `PchSetup` @ `0x697` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART0 Settings | Hardware Flow Control | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x6a2` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART0 Settings | DMA Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x69f` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART0 Settings | Power Gating | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x6a5` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART0 Settings | D0->D3 idle timeout (screen off) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x383` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART0 Settings | D0->D3 idle timeout (screen on) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x385` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART1 Settings | Hardware Flow Control | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x6a3` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART1 Settings | DMA Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x6a0` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART1 Settings | Power Gating | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x6a6` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART1 Settings | D0->D3 idle timeout (screen off) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x387` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART1 Settings | D0->D3 idle timeout (screen on) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x389` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART2 Settings | Hardware Flow Control | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x6a4` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART2 Settings | DMA Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x6a1` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART2 Settings | Power Gating | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `PchSetup` @ `0x6a7` (1) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART2 Settings | D0->D3 idle timeout (screen off) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x38b` (2) |
| Advanced > PCH-IO Configuration > SerialIo Configuration > Serial IO UART2 Settings | D0->D3 idle timeout (screen on) | 1 … 10000 (step 0) | 200 | `Setup` @ `0x38d` (2) |
| Advanced > PCH-IO Configuration > USB Configuration | XHCI Compliance Mode | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x03e` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | xDCI Support | Disabled (0x0) \| Enabled (0x1) | 0 | `PchSetup` @ `0x042` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB2 PHY Sus Well Power Gating | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x6e5` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB Overcurrent | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x03f` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB Overcurrent Lock | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x040` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB Port Disable Override | Disabled (0x0) \| Select Per-Pin (0x1) | 1 | `PchSetup` @ `0x023` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB SS Physical Connector #0 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x034` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB SS Physical Connector #1 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x035` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB SS Physical Connector #2 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x036` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB SS Physical Connector #3 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x037` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB SS Physical Connector #4 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x038` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB SS Physical Connector #5 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x039` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB SS Physical Connector #6 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x03a` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB SS Physical Connector #7 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x03b` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB SS Physical Connector #8 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x03c` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB SS Physical Connector #9 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x03d` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #0 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x024` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #1 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x025` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #2 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x026` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #3 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x027` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #0 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x028` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #5 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x029` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #6 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x02a` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #7 | Disabled (0x0) \| Enabled (0x1) | 1 | `PchSetup` @ `0x02b` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #8 | Disabled (0x0) \| Enabled (0x1) | 1 | `PchSetup` @ `0x02c` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #9 | Disabled (0x0) \| Enabled (0x1) | 1 | `PchSetup` @ `0x02d` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #10 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x02e` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #11 | Disabled (0x0) \| Enabled (0x1) | Disabled | `PchSetup` @ `0x02f` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #12 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x030` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB HS Physical Connector #13 | Disabled (0x0) \| Enabled (0x1) | Enabled | `PchSetup` @ `0x031` (1) |
| Advanced > PCH-IO Configuration > USB Configuration | USB Sensor Hub | Enabled (0x1) \| Disabled (0x0) | Disabled | `Setup` @ `0x04a` (1) |
