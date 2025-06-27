import os
import sys
import time
import secrets
import json
import hashlib
from getpass import getpass
import subprocess

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt" or os.name == "win32":
        os.system("cls")
    else:
        print("This OS is unsupported by Kode! Please try again later.")
        time.sleep(2)
        sys.exit()

def hasher(input_str: str) -> str:
    return hashlib.sha256(input_str.encode('utf-8')).hexdigest()

def logoloader():
    clear()
    logo = r"""
                                          ,---,  
       ,--.                              ,`--.' |  
   ,--/  /|                              |   :  :  
,---,': / '               ,---,          '   '  ;  
:   : '/ /   ,---.      ,---.'|          |   |  |  
|   '   ,   '   ,'\     |   | :          '   :  ;  
'   |  /   /   /   |    |   | |   ,---.  |   |  '  
|   ;  ;  .   ; ,. :  ,--.__| |  /     \ '   :  |  
:   '   \ '   | |: : /   ,'   | /    /  |;   |  ;  
|   |    ''   | .; :.   '  /  |.    ' / |`---'. |  
'   : |.  \   :    |'   ; |:  |'   ;   /| `--..`;  
|   | '_\.'\   \  / |   | '/  ''   |  / |.--,_     
'   : |     `----'  |   :    :||   :    ||    |`.  
;   |,'              \   \  /   \   \  / `-- -`, ; 
'---'                 `----'     `----'    '---`
"""
    print(logo)
    input("")
    clear()

def backupcode(username, password):
    clear()
    random_backup_code = secrets.token_hex(16)
    print(f"Great {username}! Here’s your backup code for password recovery:\n{random_backup_code}")
    input("This message will only be shown once. Press Enter to continue: ")
    data_to_dump = {
        "username": hasher(username),
        "password": hasher(password),
        "backup_code": hasher(random_backup_code)
    }
    os.makedirs("Logs and Data", exist_ok=True)
    with open("Logs and Data/users.json", "w") as file:
        json.dump(data_to_dump, file, indent=4)
    notewriting()

def signup():
    clear()
    username = input("Welcome to Kode! Please type a username: ")
    password = getpass("Please enter a password: ")
    if len(password) < 8:
        ask_for_safe_pass = input("Your password has less than 8 characters! Are you sure you want to continue (yes/no)? ").lower().strip()
        if "y" in ask_for_safe_pass:
            backupcode(username, password)
        else:
            signup()
    else:
        backupcode(username, password)

def filecreator():
    input("temp")

def editor():
    input("temp")

def filedeleter():
    input("temp")

def settings():
    input("temp")

def credits():
    input("temp")

def neofetch_surprise():
    try:
        subprocess.run(["neofetch"], check=True)
    except FileNotFoundError:
        print("Installing neofetch...")
        subprocess.run(["sudo", "apt", "install", "-y", "neofetch"], check=True)
        subprocess.run(["neofetch"])
    except Exception as e:
        print(f"Neofetch surprise failed: {e}")
    input("Press Enter to continue...")

def notewriting():
    logoloader()
    whattodo = input(">> ").lower().strip()
    
    if whattodo == "info":
        clear()
        help_text = """
Info Menu for Kode!
---------------------------
new      - Creates a new file
edit     - Edits a file
del      - Deletes a file
setting  - Opens the settings
credits  - Show the credits
info     - Shows this help menu
neofetch - ✨ (Only for Linux/WSL users!)
"""
        input(f"{help_text}\nPress Enter to continue: ")
    elif whattodo == "new":
        filecreator()
    elif whattodo == "edit":
        editor()
    elif whattodo == "del":
        filedeleter()
    elif whattodo == "settings":
        settings()
    elif whattodo == "credits":
        credits()
    elif whattodo == "neofetch" and os.name == "posix":
        neofetch_surprise()
    else:
        input("Unknown command. Press Enter to return.")
    
    notewriting()  # loop back for next command

if __name__ == "__main__":
    try:
        signup()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
