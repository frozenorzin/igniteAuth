
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
    3. 🧪 Authenticates against bcrypt-hashed values stored in `.env`
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





from flask import Flask, request, jsonify, session
from dotenv import load_dotenv
import os
import bcrypt

from flask_cors import CORS

from CORE.command_engine import command_verifyer









app = Flask(__name__)
app.secret_key = os.urandom(24)  # Temporary key for session handling


CORS(app)


load_dotenv()

# === Environment Credentials ===
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_TOKEN_HASH = os.getenv("ADMIN_TOKEN_HASH")

@app.route('/login_commander', methods=['POST'])
def login_commander():
    # getting JSON information from UI 
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Verification of username and password (for now token in env)
    if username != ADMIN_USERNAME:
        return jsonify({"status": "failure", "message": "Unknown commander"}), 401

    if not bcrypt.checkpw(password.encode(), ADMIN_TOKEN_HASH.encode()):
        return jsonify({"status": "failure", "message": "Invalid password"}), 401

    # Session-based authentication (temp, replace with JWT in v0.3.1)
    session['commander'] = username
    return jsonify({"status": "success", "message": "Commander verified"}), 200
    

@app.route('/status', methods=['GET'])
def system_status():
    if 'commander' not in session:
        return jsonify({"status": "⛔", "message": "Unauthorized access"}), 403
    return jsonify({"status": "🟢", "message": f"Welcome Commander {session['commander']}"}), 200






@app.route('/verify_command', methods = ['POST'])

def command_verify():
            # re- verification of security of session
    # active session user can only use this ,,, 

    """

            there is a story going on here at this step,   so we will attack it soon.. for now ,, comment session and commander lines 
    

    """

    test = 0   # update this to test the exact model of session handling , current 0 , bypassing the token system 
    
    if test ==1:
        
        if 'commander' not in session: 
            return jsonify({"status": "⛔", "message": "Unauthorized access"}), 403
        
    data = request.get_json()
    session_token = data.get("token")
    intent = data.get("intent")
    command = data.get("command")
    target_node = data.get("target_node")
#function within core.command_engine =>  def command_verifyer(session_token: str, intent: str, command: str, target_node: str) -> str :
    
    result = command_verifyer(session_token, intent, command, target_node)
    
    return jsonify({"result":result})








if __name__ == '__main__':
    app.run(debug=True)
