# core/command_engine.py
# 🧠 Command-Intent Verifier — Ensures secure logic validation

from time import sleep
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auth.token_handler import verify_session_token
from config.maps import COMMAND_INTENT, ALLOWED_COMMANDS, TARGET_NODE_MAP



# Add root directory to system path




def command_verifyer(session_token: str, intent: str, command: str, target_node: str) -> str :
    print("\n🧠 igniteAuth — Verifying Command Context...")

    # Step 1: Session trust check
    if not verify_session_token(session_token):
        return "❌ REJECTED: Invalid session/admin token."

    # Step 2: Intent validity
    if intent not in COMMAND_INTENT:
        return "❌ REJECTED: Unknown intent."

    # Step 3: Command validity
    expected_task_id = COMMAND_INTENT[intent]
    actual_task_id = ALLOWED_COMMANDS.get(command)

    if actual_task_id != expected_task_id:
        return "❌ REJECTED: Command does not match intent-purpose map."

    # Step 4: Target node validity
    if target_node not in TARGET_NODE_MAP:
        return "❌ REJECTED: Unknown target node."

    sleep(1.5)
    return f"✅ APPROVED: '{command}' under '{intent}' will execute on {TARGET_NODE_MAP[target_node]}."
"""
def main():
    
   username = "root@igniteAuth"
   token = "Token@ignite_auth_a1"
   intent = "emergency"
   command = "reboot_firmware"
   target_node = "addr_dev1"
   result =  command_verifyer(token, intent, command, target_node) 


   print("result of command_verifyer for given command: ", result)


if __name__ == "__main__":
    main()
 """
