

# last backup after JWT misfire... 



"""
────────────────────────────────────────────────────────────
🛰️  server.py — IgniteAuth Control Plane API
────────────────────────────────────────────────────────────

🕒 Timestamp: 3:25 AM | 30/06/2025

📌 Overview:
This module acts as the backend command/control server for IgniteAuth, 
handling login authentication and acting as the routing point for command 
verification and future node control logic.

✅ Work Done So Far:

    1. 🔐 Implemented /login_commander endpoint using Flask
    2. 📩 Accepts POST request with JSON payload (username & password)
    3. 🧪 Authenticates against bcrypt-hashed values stored in .env
    4. 💬 Returns success/failure response in JSON
    5. 🧱 Prepared structure for:
           - Multi-admin support (via DB in future)
           - Token-based command control plane
           - Separation of dashboard & logic layers

🚧 Pending in v0.3:
    - Add JWT or session token generation after login
    - Integrate command verification endpoint
    - Connect Streamlit dashboard for live interactions
    - Introduce database registry for admins and tokens

🧠 Philosophy:
    “Not just a login page — it’s the command throne.”

────────────────────────────────────────────────────────────
"""




# IgniteAuth — server.py 🛰️
"""
🧠 Secure Flask backend for login + command authentication
"""

# server.py — IgniteAuth V0.3 (backup version)

from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import bcrypt
from flask_cors import CORS
from CORE.command_engine import command_verifyer
from utils.logger import log_event
from flask_jwt_extended import JWTManager, create_access_token
from datetime import timedelta

app = Flask(__name__)
load_dotenv()

app.secret_key = os.getenv("APP_SECRET_KEY", "supersecretdevkey")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "jwt-secret-key")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)
CORS(app)

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_TOKEN_HASH = os.getenv("ADMIN_TOKEN_HASH")

@app.route('/login_commander', methods=['POST'])
def login_commander():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username != ADMIN_USERNAME:
        return jsonify({"status": "failure", "message": "Unknown commander"}), 401

    if not bcrypt.checkpw(password.encode(), ADMIN_TOKEN_HASH.encode()):
        return jsonify({"status": "failure", "message": "Invalid password"}), 401

    token = create_access_token(identity=username)
    return jsonify({
        "status": "success",
        "message": "Commander verified",
        "token": token
    }), 200

@app.route('/verify_command', methods=['POST'])
def command_verify():
    data = request.get_json()
    session_token = data.get("token")
    intent = data.get("intent")
    command = data.get("command")
    target_node = data.get("target_node")
    commander_name = data.get("username", "Unverified")  # 👈 Use value from client

    result = command_verifyer(session_token, intent, command, target_node)

    try:
        log_event(commander_name, command, target_node, result)
        print(f"[✔] Logged event for {commander_name}")
    except Exception as e:
        print(f"[Logger Error] {e}")

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
