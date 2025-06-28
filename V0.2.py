
                                         #                  IgniteAuth V0.2



  """
────────────────────────────────────────────────────────────
🔥 igniteAuth v0.2 — Secure Command Gateway (Prototype Build)
────────────────────────────────────────────────────────────

📌 Overview:
    A battlefield-grade command authentication layer designed 
    for embedded or simulated systems requiring admin validation, 
    intent-based access, and subsystem targeting.

📦 Features Implemented in v0.2:

    1. 🔐 Bcrypt-based admin token exchange via `.env` for authentication
    2. 🧠 Intent ↔ Command ↔ Target validation (mapped via task IDs)
    3. 🎯 Target node abstraction (e.g., sensors, UARTs, actuators)
    4. ⚙️ Command execution simulation with node engagement
    5. 📝 System event logging to `event.log` with full metadata:
            - Timestamp
            - Username
            - Command
            - Target Node
            - Result (✅ or ❌)

🛠 Use Case:
    - Prototype command plane for IoT or microcontroller security systems
    - CLI-based simulation with potential for Flask/Streamlit integration

🧩 Next Goals (v0.3+ Preview):
    - Real-time token generation and expiration
    - Multi-admin support via registry or DB
    - Log archival & viewer interface
    - API endpoints for remote command calls

Philosophy:
             “Not speed, but security. Not syntax, but intent.”

────────────────────────────────────────────────────────────
"""






                                                            # goals V 0.2 
"""

                                        1. Real time data and admin auth token exchange with simple algorithms  ✅ 
                                        2. Commanders and targets to be defined more clearly and securely (env, DB with salt) ✅
                                        3. Logging and monitoring triggers to be logged and saved to event.log file  
                                        4. where can we use Flask and streamlit to be decided ==  > during dynamic token exchange 
                                        


"""

                                   # Token exchange of Admin users via .env file


                                # igniteAuth v0.2 — Admin Token Exchange + Command-Intent Verification

import bcrypt
import os
from dotenv import load_dotenv
from time import sleep
import sys
from datetime import datetime 




load_dotenv()

# === Admin Token Details ===
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_TOKEN_HASH = os.getenv("ADMIN_TOKEN_HASH")

# === Intent and Command Maps ===
COMMAND_INTENT = {
    "emergency": "task_id_a",
    "test_cases": "task_id_b",
    "criticality_testing": "task_id_c"
}

ALLOWED_COMMANDS = {
    "reboot_firmware": "task_id_a",
    "run_self_test": "task_id_b",
    "powerline_diagnostics": "task_id_c"
}

# === Target Node Map ===
TARGET_NODE_MAP = {
    "addr_dev1": "node_1",      # e.g. sensor
    "addr_dev2": "node_2",      # e.g. UART
    "addr_dev3": "node_3"       # e.g. actuator
}

# === Token Hash Generator (Optional Dev Utility) ===
def generate_admin_token(admin_user, raw_token):
    hashed = bcrypt.hashpw(raw_token.encode(), bcrypt.gensalt())
    print(f"\n🔐 ADMIN_HASHED_TOKEN = {hashed.decode()}  ← Paste this into your .env")
    print(f"🔑 Original token for {admin_user} = {raw_token}")

# === Admin Identity Verifier ===
def verify_admin(user, token):
    if user != ADMIN_USERNAME:
        return False
    return bcrypt.checkpw(token.encode(), ADMIN_TOKEN_HASH.encode())

# === Session Token Verifier (reuses admin token) ===
def verify_session_token(session_token):
    return bcrypt.checkpw(session_token.encode(), ADMIN_TOKEN_HASH.encode())

# === Command Verifier: Intent ↔ Command ↔ Node Logic ===
def command_verifyer(session_token, intent, command, target_node):
    print("\n🧠 igniteAuth — Verifying Command Context...")

    # Step 1: Session trust check
    if not verify_session_token(session_token):
        return "❌ REJECTED: Invalid session/admin token."

    # Step 2: Intent validation
    if intent not in COMMAND_INTENT:
        return "❌ REJECTED: Unknown intent."

    # Step 3: Command validity
    expected_task_id = COMMAND_INTENT[intent]
    actual_task_id = ALLOWED_COMMANDS.get(command)

    if actual_task_id != expected_task_id:
        return "❌ REJECTED: Command does not match intent-purpose map."

    # Step 4: Node verification
    if target_node not in TARGET_NODE_MAP:
        return "❌ REJECTED: Unknown target node."
    sleep(1.5)
    return f"✅ APPROVED: '{command}' under '{intent}' will execute on {TARGET_NODE_MAP[target_node]}."



# === Command Execution Functions ===

def reboot_firmware():
    print("🔄 Firmware reboot initiated...")

def run_self_test():
    print("🧪 Running self-test sequence...")

def powerline_diagnostics():
    print("⚡ Performing powerline diagnostics...")


# === Node Execution Simulations ===

def node_1():
    print("📡 node_1 (sensor) engaged.")

def node_2():
    print("🔌 node_2 (UART module) engaged.")

def node_3():
    print("⚙️ node_3 (actuator) engaged.")


# === Execution Maps ===

COMMAND_EXEC_MAP = {
    "reboot_firmware": reboot_firmware,
    "run_self_test": run_self_test,
    "powerline_diagnostics": powerline_diagnostics
}

NODE_EXEC_MAP = {
    "addr_dev1": node_1,
    "addr_dev2": node_2,
    "addr_dev3": node_3
}


# === Trigger Combined Execution ===

def trigger_node_command(command, target_node):
    print("\n🚀 Executing command on target node...\n")
    sleep(1.5)

    node_func = NODE_EXEC_MAP.get(target_node)
    if node_func:
        node_func()
    else:
        print("❌ Target node has no associated execution function.")
        return

    cmd_func = COMMAND_EXEC_MAP.get(command)
    if cmd_func:
        cmd_func()
    else:
        print("❌ Command not recognized for execution.")





# logging and monitoring 



def log_event(username, command, target, response):
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{timestamp} | User: {username} | Cmd: {command} | Target: {target} | Result: {response}\n"

    with open("event.log", "a", encoding="utf-8") as logfile:
        logfile.write(log_line)











# === Main Execution ===
def main():
    """
    # Uncomment to generate admin hash
    admin_user = "root@igniteAuth"
    raw = "Token@ignite_auth_a1"
    generate_admin_token(admin_user, raw)
    return
    """

    print("\n🚨 igniteAuth v0.2 — Admin Gateway\n")
    user = sys.argv[1]
    token = sys.argv[2]

    print("\nVerifying commander...")
    sleep(1.5)

    if not verify_admin(user, token):
        print("❌ System abort: Invalid user or token.")
        return

    print("✅ Commander verified.")

    # Collect mission parameters
    intent = input("Enter command intent (emergency / test_cases / criticality_testing): ").strip()
    command = input("Enter command to execute: ").strip()
    target_node = input("Enter target node (addr_dev1 / addr_dev2 / addr_dev3): ").strip()

    result = command_verifyer(token, intent, command, target_node)
    print(result)
    

     
    log_event(user, command, target_node, result)


    if result.startswith("✅ APPROVED"):
        trigger_node_command(command, target_node)

    

if __name__ == "__main__":
    main()


    












