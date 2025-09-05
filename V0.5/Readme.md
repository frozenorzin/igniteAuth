# 🚀 IgniteAuth v0.5 – Draft Agenda

## 🔹 Overview
IgniteAuth is a lightweight authentication and command-control framework designed for secure execution of binaries across target nodes.  
Version **0.5** is a major step up from v0.4, introducing secure coding practices, user management, and MERN stack integration.

---

## ✅ IgniteAuth v0.4 Features
- **JWT session management** → 1-hour expiry, stored in `localStorage`.  
- **Single admin login** (credentials in `.env`).  
- **Command execution API** → executes one assigned binary (hardcoded).  
- **Event monitoring** → tracks command execution & status.  
- **Secure logout mechanism**.  
- **Simple minimal design**.

### ⚠️ v0.4 Demerits
1. Hardcoded password for admin inside `.env`.  
2. Codebase more AI-generated than best-practice driven.  
3. Single binary execution only.  
4. Weak authorization model.  
5. Limited login & execution monitoring.  

---

## 🔹 IgniteAuth v0.5 Goals
1. **Security Standards**  
   - Safe execution of binaries with secure coding practices.  
   - Sandboxed execution, least privilege principle.  
   - Audit logging of all actions.  

2. **MERN Stack Integration**  
   - **MongoDB** → store users, roles, nodes, logs.  
   - **Express.js / Node.js** → backend auth + API.  
   - **React.js** → frontend dashboard.  

3. **User Management**  
   - Multiple roles (Admin, Operator, Guest).  
   - Hashed & salted passwords (bcrypt/argon2).  
   - Optional MFA for admin login.  

4. **Target Node Linkers**  
   - Store node metadata (ID, hostname, allowed commands).  
   - Dynamic configuration instead of hardcoding.  

5. **Authentication & Authorization**  
   - JWT + refresh tokens.  
   - RBAC (role-based access control).  
   - Fine-grained command permissions per user & node.  

6. **Command Control**  
   - Support multiple binaries.  
   - Secure wrappers in C for system-level controls (e.g., Windows Firewall).  
   - Input validation & safe parameter handling.  

---

## 🔹 Example Pipeline (IgniteAuth v0.5)
1. **Login** → Username + password → JWT issued.  
2. **User Role Fetch** → DB returns role + node permissions.  
3. **Dashboard Access** → User sees only allowed target nodes.  
4. **Command Execution** → Auth middleware validates → binary executed securely.  
5. **Audit Log** → Store command, timestamp, and output in DB.  
6. **Monitoring** → Admin dashboard shows sessions, logs, failures.  

---

## 🔹 Roadmap
- **Phase 1** → Setup MERN & DB schema for users/nodes/logs.  
- **Phase 2** → Implement secure login + RBAC.  
- **Phase 3** → Redesign command execution (multi-node, multi-command).  
- **Phase 4** → Advanced monitoring & audit logs.  
- **Phase 5** → Security hardening (sandboxing, MFA, secret management).  

---

## 🔹 License
MIT License (to be confirmed).  

---

## 📌 Notes
- This is a **draft agenda** for IgniteAuth v0.5.  
- The final implementation will follow **secure coding practices** and **manual hardening**, reducing AI-dependency from earlier versions.  
