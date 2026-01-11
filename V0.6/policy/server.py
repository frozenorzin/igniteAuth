# python - ./policy/server.py



"""
            ===========================================================
                             IgniteAuth Policy Server
            ===========================================================

Information:

1. Acts as the authoritative policy decision point (PDP)
   for the IgniteAuth control plane.

2. Receives execution requests from the core system over
   HTTP in JSON format containing:
      - SID     : Session / Subject identifier
      - INTENT  : High-level requested operation
      - COMMAND : Low-level executable action
      - TARGET  : Subsystem to be acted upon

3. Validates incoming requests using a strict JSON schema
   to ensure structural integrity and prevent malformed or
   unexpected inputs.

4. Evaluates requests against predefined security policies,
   including:
      - Whitelisted intents, commands, and targets
      - Intent-to-command bindings
      - Intent-to-target bindings

5. Returns an explicit allow / deny decision with a reason,
   ensuring the control plane never executes actions based
   on implicit trust or local input.

6. Designed to remain stateless and deterministic, making
   it suitable for embedded control-plane enforcement,
   secure orchestration, and policy-driven execution models.

Note:
- This server NEVER executes system binaries.
- It only makes authorization decisions.
- Execution is strictly handled by the core system after
  receiving an explicit allow decision.

===========================================================
"""


# code area

from flask import Flask,request,jsonify

from policy_engine import validate_and_evaluate

app = Flask(__name__)


@app.route("/policy_engine", methods = ["POST"] )

def policy():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    decision = validate_and_evaluate(data)

    return jsonify(decision.to_dict()), 200


if __name__=="__main__":
    app.run(host="127.0.0.1", port=2000, debug=True)



    