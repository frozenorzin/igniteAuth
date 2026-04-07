# igniteAuth 🔐  
A lightweight control plane security framework for intent-driven access and policy enforcement.

## ❗ Problem

Modern systems often rely on scattered authentication logic and inconsistent access control.

- APIs validate identity but not intent  
- Authorization rules are hardcoded and fragmented  
- No clear control plane for enforcing decisions  

This leads to:
- insecure command execution  
- poor auditability  
- difficulty scaling secure systems

## 🚀 Solution

igniteAuth introduces a structured control plane that:

- Maps user intent → validated actions  
- Enforces policy before execution  
- Routes commands securely across system layers  
- Logs every decision for audit and forensics  

It separates:
- **Decision logic (control plane)**  
- **Execution logic (data plane)**

## 🧩 Core Features

- 🔐 Intent-based validation using hashed representations  
- ⚙️ Role-based access control (RBAC)  
- 🔄 Secure command routing engine  
- 📜 Immutable audit logging  
- 🧠 Modular policy enforcement layer  
- 🌐 API interface for remote command validation  
- 🧱 Embedded-ready control core (C)

## 🧪 Example Flow

1. Client sends a command request with token  
2. Intent is hashed and validated  
3. Policy engine checks role + permissions  
4. If valid → command routed to execution  
5. Event is logged (success/failure)  

Invalid requests trigger:
- fallback logic  
- audit logging  
- no execution

## 📖 Version History

### v0.1 — Simulation Core
- Admin verification  
- Intent-to-task validation  
- Secure command routing  
- Simulated execution  

### v0.2 — API + Logging Layer
- Flask REST API  
- JSON token structure  
- Immutable logging  
- Fail-safe fallback  

### v0.3 — Server Integration
- JWT token generation  
- Session management  
- Event logging  

### v0.4 — Embedded Control Core (Current 🔥)
- Secure command execution in C  
- CLI-based admin verification  
- Modular routing functions  
- Memory-safe structures  
- Ready for MCU deployment (STM32 / ESP32)

## 📌 Summary

igniteAuth is not just an authentication layer.

It is a control plane system that ensures:
- only valid intent becomes execution  
- every action is verifiable  
- policies are enforced consistently across environments