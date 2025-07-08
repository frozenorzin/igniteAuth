#!python3/auth/token_handler.py


# auth/token_handler.py

"""

                                ********  How to Use in main.py or app.py ********

       from auth.token_handler import (
       generate_admin_token,
       verify_admin,
       verify_session_token
)
            
"""


import bcrypt
import os
from dotenv import load_dotenv
import sys

load_dotenv()

# === Load Admin Credentials from .env ===
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_TOKEN_HASH = os.getenv("ADMIN_TOKEN_HASH")


# === Admin Token Hash Generator (for developer use only) ===
def generate_admin_token(admin_user: str, raw_token: str) -> None:
    hashed = bcrypt.hashpw(raw_token.encode(), bcrypt.gensalt())
    print(f"\n🔐 ADMIN_HASHED_TOKEN = {hashed.decode()}  ← Paste this into your .env")
    print(f"🔑 Original token for {admin_user} = {raw_token}")


# === Verify Admin Credentials ===
def verify_admin(user: str, token: str) -> bool:
    if user != ADMIN_USERNAME:
        return False
    return bcrypt.checkpw(token.encode(), ADMIN_TOKEN_HASH.encode())


# === Verify Session Token (reuse for command context) ===
def verify_session_token(session_token: str) -> bool:
    return bcrypt.checkpw(session_token.encode(), ADMIN_TOKEN_HASH.encode())


# This is the main() function if need to test the script within same file         
def  main(): 
    username = sys.argv[1] 
    token = sys.argv[2]
                    
    res_1 = verify_admin(username, token)
    res_2 = verify_session_token(token)

    print(f"output@verify_admin() = {res_1}")
    print(f"output@verify_session_token() = {res_2}")

if __name__ == "__main__":
    main()


