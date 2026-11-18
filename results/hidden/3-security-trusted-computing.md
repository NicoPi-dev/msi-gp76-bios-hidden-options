# Security > Trusted Computing

Category: **Hidden - MSI advanced menu** - 13 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Security > Trusted Computing | Disable Block Sid | Enabled (0x1) \| Disabled (0x0) | Disabled | `Setup` @ `0x6a5` (1) |
| Security > Trusted Computing | Device Select | TPM 1.2 (0x0) \| TPM 2.0 (0x1) \| Auto (0x2) | Auto | `Setup` @ `0x697` (1) |
| Security > Trusted Computing | SHA-1 PCR Bank | Disabled (0x0) \| Enabled (0x1) | 0 | `Setup` @ `0x69e` (1) |
| Security > Trusted Computing | SHA256 PCR Bank | Disabled (0x0) \| Enabled (0x2) | 2 | `Setup` @ `0x69f` (1) |
| Security > Trusted Computing | Pending operation | None (0x0) \| TPM Clear (0x1) | None | `Setup` @ `0x686` (1) |
| Security > Trusted Computing | Platform Hierarchy | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x693` (1) |
| Security > Trusted Computing | Storage Hierarchy | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x694` (1) |
| Security > Trusted Computing | Endorsement Hierarchy | Disabled (0x0) \| Enabled (0x1) | Enabled | `Setup` @ `0x695` (1) |
| Security > Trusted Computing | TPM 2.0 UEFI Spec Version | TCG_1_2 (0x1) \| TCG_2 (0x2) | TCG_2 | `Setup` @ `0x692` (1) |
| Security > Trusted Computing | Physical Presence Spec Version | 1.2 (0x0) \| 1.3 (0x1) | 1.3 | `Setup` @ `0x6a4` (1) |
| Security > Trusted Computing | TPM 2.0 InterfaceType | CRB (0x0) \| TIS (0x1) | CRB | `Setup` @ `0x696` (1) |
| Security > Trusted Computing | Device Select | TPM 1.2 (0x0) \| TPM 2.0 (0x1) \| Auto (0x2) | Auto | `Setup` @ `0x697` (1) |
| Security > Trusted Computing | Disable Block Sid | Enabled (0x1) \| Disabled (0x0) | Disabled | `Setup` @ `0x6a5` (1) |
