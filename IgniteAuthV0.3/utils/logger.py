# 📘 utils/logger.py — Handles event logging in igniteAuth system

from datetime import datetime
import os

LOG_FILE_PATH = os.path.join("logs", "event.log")  # Futureproofed path

def log_event(username: str, command: str, target: str, response: str) -> None:
    """
    Logs every critical system event with:
    - Timestamp
    - Username
    - Executed Command
    - Target Node
    - Result Message
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{timestamp} | User: {username} | Cmd: {command} | Target: {target} | Result: {response}\n"

    os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)  # Auto-create logs dir if not present

    with open(LOG_FILE_PATH, "a", encoding="utf-8") as logfile:
        logfile.write(log_line)
    return "Logged attempt successfully"




