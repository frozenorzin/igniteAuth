# config/maps.py
# 📍 Node and Command Mapping Registry for igniteAuth system



# === Intent to Task ID Mapping ===
COMMAND_INTENT = {
    "emergency": "task_id_a",
    "test_cases": "task_id_b",
    "criticality_testing": "task_id_c"
}

# === Allowed Commands to Task ID Mapping ===
ALLOWED_COMMANDS = {
    "reboot_firmware": "task_id_a",
    "run_self_test": "task_id_b",
    "powerline_diagnostics": "task_id_c"
}

# === Address-to-Node Identifier Mapping ===
TARGET_NODE_MAP = {
    "addr_dev1": "node_1",  # Sensor
    "addr_dev2": "node_2",  # UART
    "addr_dev3": "node_3"   # Actuator
}
