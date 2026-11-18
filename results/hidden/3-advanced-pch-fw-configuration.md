# Advanced > PCH-FW Configuration

Category: **Hidden - MSI advanced menu** - 24 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > PCH-FW Configuration | ME State | Disabled (0x0) \| Enabled (0x1) | Enabled | `MeSetupStorage` @ `0x002` (1) |
| Advanced > PCH-FW Configuration | ME Unconfig on RTC Clear | Disabled (0x0) \| Enabled (0x1) | Enabled | `MeSetup` @ `0x012` (1) |
| Advanced > PCH-FW Configuration | Comms Hub Support | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x006` (1) |
| Advanced > PCH-FW Configuration | JHI Support | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x016` (1) |
| Advanced > PCH-FW Configuration | Extend CSME Measurement to TPM-PCR | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x02c` (1) |
| Advanced > PCH-FW Configuration | Core Bios Done Message | Disabled (0x0) \| Enabled (0x1) | Enabled | `MeSetup` @ `0x013` (1) |
| Advanced > PCH-FW Configuration > Anti-Rollback SVN Configuration | Automatic HW-Enforced Anti-Rollback SVN | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x02b` (1) |
| Advanced > PCH-FW Configuration > Anti-Rollback SVN Configuration | Set HW-Enforced Anti-Rollback for Current SVN | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetupStorage` @ `0x00c` (1) |
| Advanced > PCH-FW Configuration > FIPS Configuration | FIPS Mode Select | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetupStorage` @ `0x00b` (1) |
| Advanced > PCH-FW Configuration > Firmware Update Configuration | Me FW Image Re-Flash | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x005` (1) |
| Advanced > PCH-FW Configuration > Firmware Update Configuration | FW Update | Disabled (0x0) \| Enabled (0x1) | Enabled | `MeSetupStorage` @ `0x001` (1) |
| Advanced > PCH-FW Configuration > ME Debug Configuration | HECI Timeouts | Disabled (0) \| Enabled (1) | Enabled | `MeSetup` @ `0x007` (1) |
| Advanced > PCH-FW Configuration > ME Debug Configuration | Force ME DID Init Status | Disabled (0x0) \| 0 - Success (0x1) \| 1 - No Memory in Channels (0x2) \| 2 - Memory Init Error (0x3) | Disabled | `MeSetup` @ `0x008` (1) |
| Advanced > PCH-FW Configuration > ME Debug Configuration | CPU Replaced Polling Disable | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x009` (1) |
| Advanced > PCH-FW Configuration > ME Debug Configuration | ME DID Message | Disabled (0x0) \| Enabled (0x1) | Enabled | `MeSetup` @ `0x00a` (1) |
| Advanced > PCH-FW Configuration > ME Debug Configuration | HECI Message check Disable | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x00b` (1) |
| Advanced > PCH-FW Configuration > ME Debug Configuration | MBP HOB Skip | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x00c` (1) |
| Advanced > PCH-FW Configuration > ME Debug Configuration | HECI2 Interface Communication | Disabled (0) \| Enabled (1) | Disabled | `MeSetup` @ `0x00d` (1) |
| Advanced > PCH-FW Configuration > ME Debug Configuration | KT Device | Disabled (0) \| Enabled (1) | Enabled | `MeSetup` @ `0x00e` (1) |
| Advanced > PCH-FW Configuration > ME Debug Configuration | End Of Post Message | Disabled (0x0) \| Enabled (0x1) | Enabled | `MeSetup` @ `0x014` (1) |
| Advanced > PCH-FW Configuration > ME Debug Configuration | D0I3 Setting for HECI Disable | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x00f` (1) |
| Advanced > PCH-FW Configuration > ME Debug Configuration | MCTP Broadcast Cycle | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetup` @ `0x010` (1) |
| Advanced > PCH-FW Configuration > PTT Configuration | TPM Device Selection | dTPM (0x0) \| PTT (0x1) | PTT | `MeSetup` @ `0x02d` (1) |
| Advanced > PCH-FW Configuration > PTT Configuration | TPM 1.2 Deactivate | Disabled (0x0) \| Enabled (0x1) | Disabled | `MeSetupStorage` @ `0x006` (1) |
