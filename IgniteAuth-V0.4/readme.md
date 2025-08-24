IgniteAuth v0.4

IgniteAuth is a lightweight authentication and process control plane built on Node.js + Express + JWT.
This version introduces JWT session handling, process management, and a streamlined dashboard.

📌 Features in v0.4

JWT-based sessions: Tokens stored securely in localStorage.

No manual token entry: Dashboard now fetches sessions automatically after login.

Child process execution: Server spawns secure child processes for command execution.

Session timeout management: Auto-expiry after inactivity or logout.

Simple dashboard flow: Login → Control Panel → Logs → Logout.

⚙️ Tech Stack

Frontend: HTML, CSS, Vanilla JS

Backend: Node.js + Express

Auth: JSON Web Token (JWT)

Process Handling: Node.js child_process module
