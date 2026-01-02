IgniteAuth/
│
├── core/                          # C control plane (execution authority)
│   ├── main.c                     # Entry point / request handler
│   ├── IG_executor.c              # Executes approved subsystem binaries
│   ├── IG_executor.h
│
├── include/                       # Shared headers (C)
│   ├── IG_targets.h               # Hard-mapped subsystem binaries
│   ├── IG_decision.h              # Decision struct (policy → execution)
│
├── policy/                        # Python policy engine
│   ├── policy_engine.py           # Core policy evaluation logic
│   ├── schema.py                  # JSON schema validation
│   ├── decision.py                # Decision object (Python-side)
│   └── server.py                  # Local policy API (Flask)
│
├── policies/                      # Static policy definitions
│   ├── intents.json               # Intent → target mapping
│   ├── permissions.json           # Token → intent mapping
│   └── schema.json                # JSON schema for policies
│
├── targets/                       # Subsystem source code (data plane)
│   ├── sub_gpio.c
│   ├── sub_uart.c
│   ├── sub_driver.c
│
├── bin/                           # Compiled subsystem binaries
│   ├── sub_gpio.exe
│   ├── sub_uart.exe
│   └── sub_driver.exe
│
├── logs/                          # Audit & execution logs
│   └── igniteauth.log
│
├── README.md                      # Architecture + methodology
└── Makefile opt                      # Build rules (C + subsystems)
