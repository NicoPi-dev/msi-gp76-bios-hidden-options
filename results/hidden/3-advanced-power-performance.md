# Advanced > Power & Performance

Category: **Hidden - MSI advanced menu** - 245 options

[Back to index](../HIDDEN_OPTIONS.md)

| Menu | Option | Values | Default | VarStore @ offset (size) |
|---|---|---|---|---|
| Advanced > Power & Performance | Intel(R) Speed Shift Technology Interrupt Control | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x1fc` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Boot performance mode | Max Battery (0x0) \| Max Non-Turbo Performance (0x1) \| Turbo Performance (0x2) | 1 | `CpuSetup` @ `0x00e` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Intel(R) SpeedStep(tm) | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x009` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Race To Halt (RTH) | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x00a` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Intel(R) Speed Shift Technology | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x00b` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Intel(R) Turbo Boost Max Technology 3.0 | Disabled (0x0) \| Enabled (0x1) | 1 | `CpuSetup` @ `0x00c` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | HDC Control | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x045` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Turbo Mode | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x011` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Platform PL1 Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x02c` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Platform PL1 Power | 0 … 4095875 (step 125) | 0 | `CpuSetup` @ `0x02d` (4) |
| Advanced > Power & Performance > CPU - Power Management Control | Platform PL1 Time Window | 0 (0x0) \| 1 (0x1) \| 2 (0x2) \| 3 (0x3) \| 4 (0x4) \| 5 (0x5) \| 6 (0x6) \| 7 (0x7) \| 8 (0x8) \| 10 (0xa) \| 12 (0xc) \| 14 (0xe) \| 16 (… | 0 | `CpuSetup` @ `0x031` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Platform PL2 Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x032` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Platform PL2 Power | 0 … 4095875 (step 125) | 0 | `CpuSetup` @ `0x033` (4) |
| Advanced > Power & Performance > CPU - Power Management Control | Power Limit 4 Override | Disabled (0x0) \| Enabled (0x1) | 0 | `CpuSetup` @ `0x025` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Power Limit 4 | 0 … 1023875 (step 125) | 0 | `CpuSetup` @ `0x026` (4) |
| Advanced > Power & Performance > CPU - Power Management Control | Power Limit 4 Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x02a` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | CPU C states | Disabled (0x0) \| Enabled (0x1) | 1 | `CpuSetup` @ `0x00f` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Enhanced C-states | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x010` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | C-State Auto Demotion | Disabled (0x0) \| C1 (0x1) \| C3 (0x2) \| C1 and C3 (0x3) | C1 and C3 | `CpuSetup` @ `0x039` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | C-State Un-demotion | Disabled (0x0) \| C1 (0x1) \| C3 (0x2) \| C1 and C3 (0x3) | C1 and C3 | `CpuSetup` @ `0x03a` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Package C-State Demotion | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x03b` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Package C-State Un-demotion | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x03c` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | CState Pre-Wake | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x038` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | IO MWAIT Redirection | Disabled (0x0) \| Enabled (0x1) | 0 | `CpuSetup` @ `0x043` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Package C State Limit | C0/C1 (0x0) \| C2 (0x1) \| C3 (0x2) \| C6 (0x3) \| C7 (0x4) \| C7S (0x5) \| C8 (0x6) \| C9 (0x7) \| C10 (0x8) \| Cpu Default (0xfe) \| Auto… | 255 | `CpuSetup` @ `0x046` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Time Unit | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 1024 ns | `CpuSetup` @ `0x22e` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Latency | 0 … 1023 (step 1) | 78 | `CpuSetup` @ `0x22f` (2) |
| Advanced > Power & Performance > CPU - Power Management Control | Time Unit | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 90 | `CpuSetup` @ `0x047` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Latency | 0 … 1023 (step 1) | 90 | `CpuSetup` @ `0x04c` (2) |
| Advanced > Power & Performance > CPU - Power Management Control | Time Unit | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 90 | `CpuSetup` @ `0x048` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Latency | 0 … 1023 (step 1) | 90 | `CpuSetup` @ `0x04e` (2) |
| Advanced > Power & Performance > CPU - Power Management Control | Time Unit | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 90 | `CpuSetup` @ `0x049` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Latency | 0 … 1023 (step 1) | 90 | `CpuSetup` @ `0x050` (2) |
| Advanced > Power & Performance > CPU - Power Management Control | Time Unit | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 90 | `CpuSetup` @ `0x04a` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Latency | 0 … 1023 (step 1) | 90 | `CpuSetup` @ `0x052` (2) |
| Advanced > Power & Performance > CPU - Power Management Control | Time Unit | 1 ns (0x0) \| 32 ns (0x1) \| 1024 ns (0x2) \| 32768 ns (0x3) \| 1048576 ns (0x4) \| 33554432 ns (0x5) | 90 | `CpuSetup` @ `0x04b` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Latency | 0 … 1023 (step 1) | 90 | `CpuSetup` @ `0x054` (2) |
| Advanced > Power & Performance > CPU - Power Management Control | Thermal Monitor | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x03d` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Interrupt Redirection Mode Selection | Fixed Priority (0x0) \| Round robin (0x1) \| Hash Vector (0x2) \| PAIR with Fixed Priority (0x4) \| PAIR with Round Robin (0x5) \| PAIR wit… | PAIR with Fixed Priority | `CpuSetup` @ `0x044` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Timed MWAIT | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x042` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | EC Turbo Control Mode | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x0c2` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | AC Brick Capacity | 90W AC Brick (0x1) \| 65W AC Brick (0x2) \| 75W AC Brick (0x3) | 90W AC Brick | `CpuSetup` @ `0x0c3` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | EC Polling Period | 1 … 255 (step 1) | 1 | `CpuSetup` @ `0x0c4` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | EC Guard Band Value | 0 … 20 (step 1) | 0 | `CpuSetup` @ `0x0c5` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | EC Algorithm Selection | 1 … 10 (step 1) | 1 | `CpuSetup` @ `0x0c6` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | Energy Performance Gain | Disabled (0x0) \| Enabled (0x1) | Disabled | `SaSetup` @ `0x0f0` (1) |
| Advanced > Power & Performance > CPU - Power Management Control | EPG DIMM Idd3N | 0 … 2000 (step 1) | 26 | `SaSetup` @ `0x0f1` (2) |
| Advanced > Power & Performance > CPU - Power Management Control | EPG DIMM Idd3P | 0 … 2000 (step 1) | 11 | `SaSetup` @ `0x0f3` (2) |
| Advanced > Power & Performance > CPU - Power Management Control | Dual Tau Boost | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x24d` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU Lock Configuration | CFG Lock | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x03e` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU Lock Configuration | Overclocking Lock | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x0da` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings | VR Power Delivery Design | AUTO (0x0) \| CML S 2+2 35W (0x1) \| CML S 2+2 58W (0x2) \| CML S 2+2 65W (0x3) \| CML S 4+2 35W (0x4) \| CML S 4+2 65W (0x5) \| CML S 6+2 … | 0 | `CpuSetup` @ `0x23a` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings | PSYS Slope | 0 … 200 (step 1) | 0 | `CpuSetup` @ `0x102` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings | PSYS Offset | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x103` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings | PSYS PMax Power | 0 … 8191 (step 1) | 0 | `CpuSetup` @ `0x104` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings | Intersil VR Command | Disabled (0x0) \| Send for IA/GT rails (0x1) \| Send for IA/GT/SA rails (0x2) | Disabled | `CpuSetup` @ `0x209` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Acoustic Noise Settings | Acoustic Noise Mitigation | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x1f3` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Acoustic Noise Settings | Pre Wake Time | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x237` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Acoustic Noise Settings | Ramp Up Time | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x238` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Acoustic Noise Settings | Ramp Down Time | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x239` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Acoustic Noise Settings | Disable Fast PKG C State Ramp for IA Domain | FALSE (0x0) \| TRUE (0x1) | FALSE | `CpuSetup` @ `0x1f4` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Acoustic Noise Settings | Slow Slew Rate for IA Domain | Fast/2 (0x0) \| Fast/4 (0x1) \| Fast/8 (0x2) \| Fast/16 (0x3) | Fast/8 | `CpuSetup` @ `0x1f8` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Acoustic Noise Settings | Disable Fast PKG C State Ramp for GT Domain | FALSE (0x0) \| TRUE (0x1) | 0 | `CpuSetup` @ `0x1f5` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Acoustic Noise Settings | Slow Slew Rate for GT Domain | Fast/2 (0x0) \| Fast/4 (0x1) \| Fast/8 (0x2) \| Fast/16 (0x3) | 0 | `CpuSetup` @ `0x1f9` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Acoustic Noise Settings | Disable Fast PKG C State Ramp for SA Domain | FALSE (0x0) \| TRUE (0x1) | FALSE | `CpuSetup` @ `0x1f6` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Acoustic Noise Settings | Slow Slew Rate for SA Domain | Fast/2 (0x0) \| Fast/4 (0x1) \| Fast/8 (0x2) | Fast/2 | `CpuSetup` @ `0x1fa` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Acoustic Noise Settings | Disable Fast PKG C State Ramp for VccIn Domain | FALSE (0x0) \| TRUE (0x1) | FALSE | `CpuSetup` @ `0x1f7` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Acoustic Noise Settings | Slow Slew Rate for VccIn Domain | Fast/2 (0x0) \| Fast/4 (0x1) \| Fast/8 (0x2) \| Fast/16 (0x3) | Fast/2 | `CpuSetup` @ `0x1fb` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | VR Config Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x107` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | AC Loadline | 0 … 62500 (step 0) | 30 | `CpuSetup` @ `0x10d` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | DC Loadline | 0 … 62500 (step 0) | 110 | `CpuSetup` @ `0x117` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | PS Current Threshold1 | 0 … 512 (step 1) | 80 | `CpuSetup` @ `0x121` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | PS Current Threshold2 | 0 … 512 (step 1) | 20 | `CpuSetup` @ `0x12b` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | PS Current Threshold3 | 0 … 512 (step 1) | 4 | `CpuSetup` @ `0x135` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | PS3 Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x13e` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | PS4 Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x143` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | IMON Slope | 0 … 200 (step 1) | 0 | `CpuSetup` @ `0x210` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | IMON Offset | 0 … 63999 (step 1) | 0 | `CpuSetup` @ `0x14e` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | IMON Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x157` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | VR Current Limit | 0 … 1023 (step 1) | 660 | `CpuSetup` @ `0x15d` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | VR Voltage Limit | 0 … 7999 (step 1) | 0 | `CpuSetup` @ `0x167` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | TDC Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x17a` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | TDC Current Limit | 0 … 32767 (step 125) | 1000 | `CpuSetup` @ `0x171` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | TDC Time Window | 1 ms (0x1) \| 2 ms (0x2) \| 3 ms (0x3) \| 4 ms (0x4) \| 5 ms (0x5) \| 6 ms (0x6) \| 7 ms (0x7) \| 8 ms (0x8) \| 10 ms (0xa) | 1 ms | `CpuSetup` @ `0x17f` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > Core/IA VR Settings | TDC Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x184` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | VR Config Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x109` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | AC Loadline | 0 … 62500 (step 0) | 0 | `CpuSetup` @ `0x111` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | DC Loadline | 0 … 62500 (step 0) | 0 | `CpuSetup` @ `0x11b` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | PS Current Threshold1 | 0 … 512 (step 1) | 80 | `CpuSetup` @ `0x125` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | PS Current Threshold2 | 0 … 512 (step 1) | 20 | `CpuSetup` @ `0x12f` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | PS Current Threshold3 | 0 … 512 (step 1) | 4 | `CpuSetup` @ `0x139` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | PS3 Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x140` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | PS4 Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x145` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | IMON Slope | 0 … 200 (step 1) | 0 | `CpuSetup` @ `0x214` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | IMON Offset | 0 … 63999 (step 1) | 0 | `CpuSetup` @ `0x152` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | IMON Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x159` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | VR Current Limit | 0 … 1023 (step 1) | 0 | `CpuSetup` @ `0x161` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | VR Voltage Limit | 0 … 7999 (step 1) | 0 | `CpuSetup` @ `0x16b` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | TDC Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x17c` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | TDC Current Limit | 0 … 32767 (step 125) | 0 | `CpuSetup` @ `0x175` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | TDC Time Window | 1 ms (0x1) \| 2 ms (0x2) \| 3 ms (0x3) \| 4 ms (0x4) \| 5 ms (0x5) \| 6 ms (0x6) \| 7 ms (0x7) \| 8 ms (0x8) \| 10 ms (0xa) | 1 ms | `CpuSetup` @ `0x181` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > GT VR Settings | TDC Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x186` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > RFI Settings | RFI Frequency Adjustment | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x1ed` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > RFI Settings | RFI Frequency Prefix | + (0x0) \| - (0x1) | 0 | `CpuSetup` @ `0x1ee` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > RFI Settings | RFI Spread Spectrum | 0.5% (0x1) \| 1% (0x2) \| 1.5% (0x3) \| 2% (0x4) \| 3% (0x5) \| 4% (0x6) \| 5% (0x7) \| 6% (0x8) | 3 | `CpuSetup` @ `0x1ef` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > RFI Settings | RFI Frequency | 0 … 1918 (step 0) | 0 | `CpuSetup` @ `0x1f0` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > RFI Settings | RFI Spread Spectrum | 0 … 100 (step 0) | 0 | `CpuSetup` @ `0x1f2` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | VR Config Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x106` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | AC Loadline | 0 … 6249 (step 0) | 0 | `CpuSetup` @ `0x10b` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | DC Loadline | 0 … 6249 (step 0) | 0 | `CpuSetup` @ `0x115` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | PS Current Threshold1 | 0 … 512 (step 1) | 80 | `CpuSetup` @ `0x11f` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | PS Current Threshold2 | 0 … 512 (step 1) | 20 | `CpuSetup` @ `0x129` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | PS Current Threshold3 | 0 … 512 (step 1) | 4 | `CpuSetup` @ `0x133` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | PS3 Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x13d` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | PS4 Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x142` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | IMON Slope | 0 … 200 (step 1) | 0 | `CpuSetup` @ `0x20e` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | IMON Offset | 0 … 63999 (step 1) | 0 | `CpuSetup` @ `0x14c` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | IMON Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x156` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | VR Current Limit | 0 … 1023 (step 1) | 0 | `CpuSetup` @ `0x15b` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | VR Voltage Limit | 0 … 7999 (step 1) | 0 | `CpuSetup` @ `0x165` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | TDC Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x179` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | TDC Current Limit | 0 … 32767 (step 125) | 0 | `CpuSetup` @ `0x16f` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | TDC Time Window | 1 ms (0x1) \| 2 ms (0x2) \| 3 ms (0x3) \| 4 ms (0x4) \| 5 ms (0x5) \| 6 ms (0x6) \| 7 ms (0x7) \| 8 ms (0x8) \| 10 ms (0xa) | 1 ms | `CpuSetup` @ `0x17e` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > System Agent VR Settings | TDC Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x183` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | VR Config Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x10a` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | AC Loadline | 0 … 62500 (step 0) | 0 | `CpuSetup` @ `0x113` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | DC Loadline | 0 … 62500 (step 0) | 0 | `CpuSetup` @ `0x11d` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | PS Current Threshold1 | 0 … 512 (step 1) | 80 | `CpuSetup` @ `0x127` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | PS Current Threshold2 | 0 … 512 (step 1) | 20 | `CpuSetup` @ `0x131` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | PS Current Threshold3 | 0 … 512 (step 1) | 4 | `CpuSetup` @ `0x13b` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | PS3 Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x141` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | PS4 Enable | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x146` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | IMON Slope | 0 … 200 (step 1) | 0 | `CpuSetup` @ `0x216` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | IMON Offset | 0 … 63999 (step 1) | 0 | `CpuSetup` @ `0x154` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | IMON Prefix | + (0x0) \| - (0x1) | + | `CpuSetup` @ `0x15a` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | VR Current Limit | 0 … 1023 (step 1) | 0 | `CpuSetup` @ `0x163` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | VR Voltage Limit | 0 … 7999 (step 1) | 0 | `CpuSetup` @ `0x16d` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | TDC Enable | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x17d` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | TDC Current Limit | 0 … 32767 (step 125) | 0 | `CpuSetup` @ `0x177` (2) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | TDC Time Window | 1 ms (0x1) \| 2 ms (0x2) \| 3 ms (0x3) \| 4 ms (0x4) \| 5 ms (0x5) \| 6 ms (0x6) \| 7 ms (0x7) \| 8 ms (0x8) \| 10 ms (0xa) | 1 ms | `CpuSetup` @ `0x182` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > CPU VR Settings > VccIn VR Settings | TDC Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x187` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Configurable TDP Boot Mode | Nominal (0x0) \| Down (0x1) \| Up (0x2) \| Deactivate (0xff) | 90 | `CpuSetup` @ `0x03f` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Configurable TDP Lock | Enabled (0x1) \| Disabled (0x0) | Disabled | `CpuSetup` @ `0x040` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | CTDP BIOS control | Enabled (0x1) \| Disabled (0x0) | Disabled | `CpuSetup` @ `0x041` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Power Limit 1 | 0 … 4095875 (step 125) | 200000 | `CpuSetup` @ `0x056` (4) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Power Limit 2 | 0 … 4095875 (step 125) | 200000 | `CpuSetup` @ `0x05a` (4) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Power Limit 1 Time Window | 0 (0x0) \| 1 (0x1) \| 2 (0x2) \| 3 (0x3) \| 4 (0x4) \| 5 (0x5) \| 6 (0x6) \| 7 (0x7) \| 8 (0x8) \| 10 (0xa) \| 12 (0xc) \| 14 (0xe) \| 16 (… | 0 | `CpuSetup` @ `0x05e` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | ConfigTDP Turbo Activation Ratio | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x05f` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Power Limit 1 | 0 … 4095875 (step 125) | 0 | `CpuSetup` @ `0x060` (4) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Power Limit 2 | 0 … 4095875 (step 125) | 0 | `CpuSetup` @ `0x064` (4) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Power Limit 1 Time Window | 0 (0x0) \| 1 (0x1) \| 2 (0x2) \| 3 (0x3) \| 4 (0x4) \| 5 (0x5) \| 6 (0x6) \| 7 (0x7) \| 8 (0x8) \| 10 (0xa) \| 12 (0xc) \| 14 (0xe) \| 16 (… | 0 | `CpuSetup` @ `0x068` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | ConfigTDP Turbo Activation Ratio | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x069` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Power Limit 1 | 0 … 4095875 (step 125) | 0 | `CpuSetup` @ `0x06a` (4) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Power Limit 2 | 0 … 4095875 (step 125) | 0 | `CpuSetup` @ `0x06e` (4) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | Power Limit 1 Time Window | 0 (0x0) \| 1 (0x1) \| 2 (0x2) \| 3 (0x3) \| 4 (0x4) \| 5 (0x5) \| 6 (0x6) \| 7 (0x7) \| 8 (0x8) \| 10 (0xa) \| 12 (0xc) \| 14 (0xe) \| 16 (… | 0 | `CpuSetup` @ `0x072` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Config TDP Configurations | ConfigTDP Turbo Activation Ratio | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x073` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | Number of P states | 0 … 40 (step 0) | 0 | `CpuSetup` @ `0x07b` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | Max P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x07c` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x07d` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x07e` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x07f` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x080` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x081` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x082` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x083` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x084` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x085` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x086` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x087` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x088` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x089` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x08a` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x08b` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x08c` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x08d` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x08e` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x08f` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x090` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x091` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x092` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x093` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x094` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x095` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x096` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x097` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x098` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x099` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x09a` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x09b` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x09c` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x09d` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x09e` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x09f` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0a0` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0a1` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0a2` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0a3` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | Max P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0a4` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0a5` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0a6` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0a7` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0a8` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0a9` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0aa` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0ab` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0ac` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0ad` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0ae` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0af` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0b0` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0b1` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0b2` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Custom P-state Table | Min P-State Ratio (Max 16 table) | 0 … 127 (step 0) | 0 | `CpuSetup` @ `0x0b3` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Power Limit 3 Settings | Power Limit 3 Override | Disabled (0x0) \| Enabled (0x1) | 0 | `CpuSetup` @ `0x01d` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Power Limit 3 Settings | Power Limit 3 | 0 … 4095875 (step 125) | 0 | `CpuSetup` @ `0x01e` (4) |
| Advanced > Power & Performance > CPU - Power Management Control > Power Limit 3 Settings | Power Limit 3 Time Window | 0 (0x0) \| 3 (0x3) \| 4 (0x4) \| 5 (0x5) \| 6 (0x6) \| 7 (0x7) \| 8 (0x8) \| 10 (0xa) \| 12 (0xc) \| 14 (0xe) \| 16 (0x10) \| 20 (0x14) \| … | 0 | `CpuSetup` @ `0x022` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Power Limit 3 Settings | Power Limit 3 Duty Cycle | 0 … 100 (step 0) | 0 | `CpuSetup` @ `0x023` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > Power Limit 3 Settings | Power Limit 3 Lock | Disabled (0x0) \| Enabled (0x1) | 1 | `CpuSetup` @ `0x024` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Energy Efficient P-state | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x037` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Package Power Limit MSR Lock | Disabled (0x0) \| Enabled (0x1) | Disabled | `CpuSetup` @ `0x02b` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Power Limit 1 Override | Disabled (0x0) \| Enabled (0x1) | 0 | `CpuSetup` @ `0x016` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Power Limit 1 | 0 … 4095875 (step 125) | 0 | `CpuSetup` @ `0x012` (4) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Power Limit 1 Time Window | 0 (0x0) \| 1 (0x1) \| 2 (0x2) \| 3 (0x3) \| 4 (0x4) \| 5 (0x5) \| 6 (0x6) \| 7 (0x7) \| 8 (0x8) \| 10 (0xa) \| 12 (0xc) \| 14 (0xe) \| 16 (… | 0 | `CpuSetup` @ `0x017` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Power Limit 2 Override | Disabled (0x0) \| Enabled (0x1) | Enabled | `CpuSetup` @ `0x018` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Power Limit 2 | 0 … 4095875 (step 125) | 0 | `CpuSetup` @ `0x019` (4) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Ratio Limit Core0 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x243` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Ratio Limit Core1 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x244` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Ratio Limit Core2 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x245` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Ratio Limit Core3 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x246` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Ratio Limit Core4 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x247` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Ratio Limit Core5 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x248` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Ratio Limit Core6 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x249` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Ratio Limit Core7 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x24a` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Core Ratio Limit0 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x0d1` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Core Ratio Limit1 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x0d2` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Core Ratio Limit2 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x0d3` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Core Ratio Limit3 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x0d4` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Core Ratio Limit4 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x0d5` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Core Ratio Limit5 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x0d6` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Core Ratio Limit6 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x0d7` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Core Ratio Limit7 Override | 0 … 255 (step 1) | 0 | `CpuSetup` @ `0x0d8` (1) |
| Advanced > Power & Performance > CPU - Power Management Control > View/Configure Turbo Options | Energy Efficient Turbo | Disabled (0x0) \| Enabled (0x1) \| Auto (0x2) | Auto | `CpuSetup` @ `0x1af` (1) |
| Advanced > Power & Performance > GT - Power Management Control | RC6(Render Standby) | Disabled (0x0) \| Enabled (0x1) | 1 | `SaSetup` @ `0x03e` (1) |
| Advanced > Power & Performance > GT - Power Management Control | Maximum GT frequency | Default Max Frequency (0xff) \| 100Mhz (0x2) \| 150Mhz (0x3) \| 200Mhz (0x4) \| 250Mhz (0x5) \| 300Mhz (0x6) \| 350Mhz (0x7) \| 400Mhz (0x8… | Default Max Frequency | `SaSetup` @ `0x04e` (1) |
| Advanced > Power & Performance > GT - Power Management Control | Disable Turbo GT frequency | Enabled (0x1) \| Disabled (0x0) | Disabled | `SaSetup` @ `0x04f` (1) |
