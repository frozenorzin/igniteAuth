# Ignite Auth V0.3 — dashboard.py

"""
            Admin dashboard 

"""


# backed up version ,, last working model ,, made on 


import streamlit as st
import requests
import os 





LOG_FILE_PATH = os.path.join("logs", "event.log")


# === Page Config ===
st.set_page_config(page_title="IgniteAuth Admin", layout="centered")

# === Session State Initialization ===
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "auth_message" not in st.session_state:
    st.session_state.auth_message = ""

# === Login Page ===
def login_page():
    st.title("IgniteAuth Admin Login")
    st.markdown("....Secure your control plane....")

    username = st.text_input("USERNAME", max_chars=20)
    password = st.text_input("PASSWORD", type="password", max_chars=20)

    if st.button("Login"):
        payload = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post("http://127.0.0.1:5000/login_commander", json=payload)
            if response.status_code == 200:
                resp_json = response.json()
                status = resp_json.get("status")
                message = resp_json.get("message")

                st.session_state.auth_message = message
                if status.lower() == "success":
                    st.success(f"Verified : {message}")
                    st.session_state.authenticated = True
                else:
                    st.error(f"Failed: {message}")
                    st.session_state.authenticated = False
            else:
                st.error(f"Server responded with error : {response.status_code}")
        except Exception as e:
            st.error(f"Server error : {e}")

# === Dashboard Control Panel ===
def dashboard():
    st.title("Control Panel: IgniteAuth V0.3")
    st.sidebar.markdown("**Session initiated: commander**")
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"authenticated": False}))

    tab1, tab2 = st.tabs(["⚙️ Subsystem Control", "📄 Event Log (server log)"])

    with tab1:
        st.markdown("## 🧠 Sub-System Control Panel")
        st.markdown("Control your nodes securely with intent verification.")

        with st.form("subsystem_form"):
            st.markdown("### 🎯 Target Node Selection")

            node_options = {
                "Sensor (node_1)": "addr_dev1",
                "UART (node_2)": "addr_dev2",
                "Actuator (Comm / node_3)": "addr_dev3"
            }
            target_node_label = st.selectbox("Select Target Node", list(node_options.keys()))
            target_node = node_options[target_node_label]

            st.markdown("---")
            st.markdown("### 📄 Command Details")

            intent = st.selectbox("Command Intent", ["emergency", "test_cases", "criticality_testing"])
            command = st.selectbox("Command to Execute", ["reboot_firmware", "run_self_test", "powerline_diagnostics"])

            token = st.text_input("Admin Session Token", value="Token@ignite_auth_a1")

            submitted = st.form_submit_button("✅ Verify Command")

            if submitted:
                payload = {
                "token": token,
                "intent": intent,
                "command": command,
                "target_node": target_node,
                "username": "root@igniteAuth"  # 👈 added hardcoded commander identity
               }
    
                try:
                    response = requests.post("http://127.0.0.1:5000/verify_command", json=payload)
                    if response.status_code == 200:
                        st.success(response.json().get("result", "✅ Command accepted"))
                    elif response.status_code == 403:
                        st.warning("🔒 Session missing or unauthorized access.")
                    else:
                        st.error(f"Server error: {response.status_code}")
                except Exception as e:
                    st.error(f"Connection error: {e}")

                
     # === Tab 2: Log Viewer ===
    with tab2:
        st.markdown("## 📄 Command Event Logs")
        st.caption("Showing only verified admin logs (User: root@igniteAuth)")

        if st.button("🔄 Refresh Log"):
            st.experimental_rerun()

        if os.path.exists(LOG_FILE_PATH):
            with open(LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
                logs = log_file.readlines()
                logs = [line for line in logs if "User: root@igniteAuth" in line]  # 💡 filter only root@igniteAuth
                logs = logs[::-1]  # Show latest first

                if logs:
                    for line in logs:
                        st.code(line.strip(), language="bash")
                else:
                    st.info("No verified admin logs found yet.")
        else:
            st.warning("No logs available yet.")
            
# === Route Control ===
if not st.session_state.authenticated:
    login_page()
else:
    dashboard()
