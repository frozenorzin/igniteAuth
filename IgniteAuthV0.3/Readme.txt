IgniteAuthV0.3/
│
├── app.py                  # Flask app starter
├── dashboard.py            # Streamlit visual layer
├── auth/
│   └── token_handler.py    # Admin & session token generation/verification
├── core/
│   └── command_engine.py   # Command-intent-purpose logic
│   └── node_executor.py    # Trigger functions for hardware nodes
├── config/
│   └── maps.py             # Command/intent/node dictionaries
│   └── env_loader.py       # Handles .env
├── logs/
│   └── event.log           # Logging storage
└── utils/
    └── logger.py           # Logging utility













 			IgniteAuth V0.3 - dashboard.py


streamlit already tuned for login and session keep 


now ....


subsystem control..... 


1.I must create sub-panel for subsystems 
2. if i click on this sub panel = > 3 buttons + 1 heading =>  1 button = each node ,,, 

3. if i click on node ,, i would get the options of intent , command and   

4. once again saying ['target_node'] is first element to be seen in UI sub dashboard , then according to choosen ones , variables can be filled 

for now ,, lets make form of 4 values ,, then send  it via POST to /verify_command in server.py , then we can choose various styles 


