# igniteAuth


# igniteAuth v0.1 🔥
**Intent-Governed Execution Control Layer for Embedded & Simulated Systems**

---

## 🔍 Project Summary

`igniteAuth` is a universal, intent-driven control layer designed to govern execution in embedded and general-purpose systems. It ensures that no command is executed without proper authorization and alignment with the system’s operational intent.

This version (`v0.1`) introduces:
- Raw admin authorization
- Intent-to-task validation
- Command filtering via task IDs
- Simulated subsystem execution
- JSON-like packet-based execution logic

---

## 🧠 Why igniteAuth?

Modern computing systems — from AI agents to embedded controllers — blindly execute any syntactically valid command, regardless of who issued it or why. This leads to:
- Security vulnerabilities
- Unauthorized firmware or actuator access
- Dangerous autonomy in critical systems

`igniteAuth` addresses this by introducing a **Battlefield Law Layer**, where commands are governed by:
- **Intent**
- **Purpose**
- **Admin Authorization**

---

## ❓ Gemini-Based Design Questions

### 1. **What types of systems will the universal control plane manage?**

- Embedded systems (ESP32, STM32, Arduino-class)
- Simulated hardware (Python CLI/console-controlled)
- IoT devices requiring OTA commands
- Future robotic agents or AI-driven systems

---

### 2. **What capabilities will the control plane offer?**

✔️ Admin-based command authentication  
✔️ Intent-purpose mapping (`COMMAND_PURPOSE`)  
✔️ Command-task consistency enforcement  
✔️ Simulated subsystem responses (motor, alarm, firmware control)  
✔️ Centralized Battlefield Law core (`battlefield_law_execute`)  
✔️ Human-readable JSON command packets

---

### 3. **How is the architecture flexible and extensible?**

- All mappings (`ADMINS`, `COMMAND_PURPOSE`, `ALLOWED_COMMANDS`) are dictionary-driven and easily expandable
- Subsystems are modular functions (plug-and-play architecture)
- Command packets can evolve into signed JSON tokens
- Future-ready for:
  - Flask REST API
  - Real-time MQTT integration
  - Microcontroller porting
  - Immutable audit logs
  - Role hierarchies (superadmin, guest)

---

## ⚙️ igniteAuth v0.1 Components

| Component         | Role                                                   |
|------------------|--------------------------------------------------------|
| `ADMINS`         | Registry of verified command issuers                   |
| `COMMAND_PURPOSE`| Maps intents to task IDs                               |
| `ALLOWED_COMMANDS`| Command-task bindings (governed by purpose)           |
| `battlefield_law_execute()` | Core execution validator                     |
| Simulated Subsystems | Firmware reboot, self-test, powerline diagnostics |

---

## 🧪 How It Works (Sample Packet)

```json
{
  "user": "root_x_t0",
  "token": "token1",
  "intent": "emergency",
  "command": "reboot_firmware"
}
