# IgniteAuth 🔐

A lightweight control plane security framework for intent-driven access and policy enforcement.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Overview

IgniteAuth is a comprehensive security framework designed to separate decision logic (control plane) from execution logic (data plane). It provides intent-based validation, role-based access control, and immutable audit logging for modern applications.

**Current Version:** v0.4 (Embedded Control Core)

## Problem

Modern systems often rely on scattered authentication logic and inconsistent access control:
- APIs validate identity but not intent
- Authorization rules are hardcoded and fragmented
- No clear control plane for enforcing decisions

This leads to:
- Insecure command execution
- Poor auditability
- Difficulty scaling secure systems

## Solution

IgniteAuth introduces a structured control plane that:
- Maps user intent → validated actions
- Enforces policy before execution
- Routes commands securely across system layers
- Logs every decision for audit and forensics

## Features

- 🔐 **Intent-Based Validation** - Uses hashed representations for secure intent validation
- ⚙️ **Role-Based Access Control (RBAC)** - Fine-grained permission management
- 🔄 **Secure Command Routing** - Safe command execution across system layers
- 📜 **Immutable Audit Logging** - Complete action tracking for compliance
- 🧠 **Modular Policy Enforcement** - Flexible policy layer for custom rules
- 🌐 **REST API Interface** - Remote command validation and management
- 🧱 **Embedded-Ready Core** - C implementation for MCU deployment (STM32 / ESP32)

## Installation

### Prerequisites
- Python 3.8+
- C compiler (for v0.4 embedded core)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/frozenorzin/igniteAuth.git
   cd igniteAuth
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Build the embedded core (optional):
   ```bash
   cd IgniteAuth-V0.4
   make build
   ```

## Quick Start

### Python API (v0.2, v0.3)
```python
from igniteauth import AuthEngine

# Initialize
auth = AuthEngine(admin_token="your_admin_token")

# Validate intent
result = auth.validate_intent(
    user_token="user_token",
    intent="execute_command",
    role="admin"
)

if result['valid']:
    print("Intent approved, executing...")
else:
    print("Intent rejected")
```

### Flask REST API
```bash
python IgniteAuthV0.3/app.py
```

Access API at `http://localhost:5000`

### Embedded C Core (v0.4)
```c
#include "igniteauth.h"

int main() {
    auth_context_t ctx;
    auth_init(&ctx);
    
    auth_result_t result = auth_validate_intent(&ctx, user_token, intent);
    
    if (result.valid) {
        auth_execute_command(&ctx, command);
    }
    
    return 0;
}
```

## Usage

### Example Flow

1. Client sends a command request with token
2. Intent is hashed and validated
3. Policy engine checks role + permissions
4. If valid → command routed to execution
5. Event is logged (success/failure)

Invalid requests trigger:
- Fallback logic
- Audit logging
- No execution

### Checking Audit Logs
```bash
tail -f event.log
```

## Architecture

IgniteAuth follows a **control plane / data plane separation** pattern:

```
┌─────────────────────────────────────────┐
│         Control Plane                   │
│  (Decision Logic, Policy Enforcement)   │
│                                         │
│  ┌─────────────┐  ┌──────────────────┐ │
│  │ Auth Engine │──│ Policy Evaluator │ │
│  └─────────────┘  └──────────────────┘ │
└─────────────────────────────────────────┘
           │
           │ (Validated Commands)
           ↓
┌─────────────────────────────────────────┐
│         Data Plane                      │
│  (Execution Logic, Command Routing)     │
│                                         │
│  ┌──────────────┐  ┌──────────────────┐│
│  │Exec Engine   │──│ Audit Logger     ││
│  └──────────────┘  └──────────────────┘│
└─────────────────────────────────────────┘
```

## Project Structure

```
igniteAuth/
├── README.md                          # This file
├── V0.1.py                           # Initial simulation core
├── V0.2.py                           # Flask API + Logging
├── IgniteAuthV0.3/                   # Server integration
│   ├── app.py                        # Flask application
│   ├── auth.py                       # Core auth logic
│   └── models.py                     # Database models
├── IgniteAuth-V0.4/                  # Embedded C core
│   ├── igniteauth.h                  # Header file
│   ├── igniteauth.c                  # Core implementation
│   └── Makefile
├── V0.5/                             # Future version (in progress)
├── V0.6/                             # Future version (in progress)
├── CPS_thesis.odt                    # Research documentation
├── Hardware Software Integration.pdf # Integration guide
└── event.log                         # Audit log file
```

## API Documentation

### Authentication Endpoint
```
POST /api/auth/validate
Content-Type: application/json

{
  "user_token": "string",
  "intent": "string",
  "role": "string"
}

Response:
{
  "valid": boolean,
  "message": "string",
  "timestamp": "ISO 8601"
}
```

### Command Execution Endpoint
```
POST /api/execute
Content-Type: application/json

{
  "command": "string",
  "auth_token": "string"
}

Response:
{
  "status": "success|failure",
  "result": "string",
  "log_id": "string"
}
```

For full API documentation, see the [API Docs](API.md).

## Version History

| Version | Focus | Key Features |
|---------|-------|--------------|
| v0.1 | Simulation Core | Admin verification, Intent validation, Command routing |
| v0.2 | API + Logging | Flask REST API, JSON tokens, Immutable logging |
| v0.3 | Server Integration | JWT generation, Session management, Event logging |
| v0.4 | Embedded Core | C implementation, CLI verification, MCU-ready |
| v0.5 | In Progress | Enhanced policy engine |
| v0.6 | In Progress | Distributed control plane |

## Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature`
3. **Commit** your changes: `git commit -m "Add feature description"`
4. **Push** to the branch: `git push origin feature/your-feature`
5. **Submit** a Pull Request

### Code Style
- Python: Follow PEP 8
- C: Follow MISRA C guidelines
- Include tests for new features
- Update documentation accordingly

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

### Getting Help
- 📖 Check the [documentation](https://github.com/frozenorzin/igniteAuth/wiki)
- 🐛 Report issues on [GitHub Issues](https://github.com/frozenorzin/igniteAuth/issues)
- 💬 Discuss ideas on [GitHub Discussions](https://github.com/frozenorzin/igniteAuth/discussions)

### Contact
- Author: [@frozenorzin](https://github.com/frozenorzin)
- Email: contact@igniteauth.dev

---

**IgniteAuth** - Secure Control Plane for Modern Systems
