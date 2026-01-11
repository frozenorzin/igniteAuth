# decision.py

class Decision:
    def __init__(self, sid, intent, command, target, allow, reason=None):
        self.sid = sid
        self.intent = intent
        self.command = command
        self.target = target
        self.allow = allow
        self.reason = reason

    def to_dict(self):
        d = {
            "sid": self.sid,
            "intent": self.intent,
            "command": self.command,
            "target": self.target,
            "allow": self.allow
        }
        if self.reason:
            d["reason"] = self.reason
        return d
