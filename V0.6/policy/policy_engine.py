#./policy/policy_engine.py

"""
                    ===========================================================
                                     IgniteAuth Policy Engine
                    ===========================================================

Information:

1. This module implements the core authorization logic for
   IgniteAuth and functions as the Policy Decision Logic
   behind the policy server.

2. It enforces strict, whitelist-based security rules on
   execution requests by validating:
      - Intent legitimacy
      - Command legitimacy
      - Target legitimacy

3. Implements binding enforcement to ensure that:
      - A command is valid only for its declared intent
      - A target is valid only for its declared intent

4. Policy evaluation is deterministic and explicit:
      - Every request results in an ALLOW or DENY decision
      - Deny decisions include a clear reason for rejection

5. Schema validation is performed before policy evaluation
   to prevent malformed or adversarial inputs from reaching
   the authorization logic.

6. This module does NOT execute any system commands or
   binaries and remains purely declarative and authoritative.

Design Principle:
- “No implicit trust, only explicit authorization.”

===========================================================
"""










# code area 



from jsonschema import validate as json_validate, ValidationError
from schema import schema
from decision import Decision


# whitelist parameters
WHITE_INTENTS = ["firmware_reboot", "reset_system", "mpu_test"]
WHITE_COMMANDS = ["rebootF", "sysReset", "mpuTest"]
WHITE_TARGETS = ["uart", "driver", "gpio"]




# =========================
# Policy bindings
# =========================

INTENT_COMMAND_MAP = {
    "firmware_reboot": {"rebootF"},
    "reset_system": {"sysReset"},
    "mpu_test": {"mpuTest"}
}

INTENT_TARGET_MAP = {
    "firmware_reboot": {"gpio", "driver"},
    "reset_system": {"driver"},
    "mpu_test": {"uart"}
}



def evaluate_policy(sid, intent, command, target):
    """Authoritative policy decision with reason"""

    if intent not in WHITE_INTENTS:
        return Decision(sid, intent, command, target, False, "Intent not allowed")

    if command not in WHITE_COMMANDS:
        return Decision(sid, intent, command, target, False, "Command not allowed")

    if target not in WHITE_TARGETS:
        return Decision(sid, intent, command, target, False, "Target not allowed")

    if command not in INTENT_COMMAND_MAP.get(intent, set()):
        return Decision(sid, intent, command, target, False, "Command not valid for intent")

    if target not in INTENT_TARGET_MAP.get(intent, set()):
        return Decision(sid, intent, command, target, False, "Target not valid for intent")

    return Decision(sid, intent, command, target, True)

def validate_and_evaluate(jsonD):

    try:
        json_validate(instance=jsonD, schema=schema)

        return evaluate_policy(
            sid = jsonD["sid"],
            intent=jsonD["intent"],
            command=jsonD["command"],
            target=jsonD["target"]
            
            
        )
    except ValidationError:
        return Decision(
            sid = jsonD.get("sid", "UNKNOWN"),
            intent = jsonD.get("intent", "UNKNOWN"),
            command = jsonD.get("command", "UNKNOWN"),
            target = jsonD.get("target", "UNKNOWN"),
            allow = False,
            reason="Schema validation failed"
        )
    