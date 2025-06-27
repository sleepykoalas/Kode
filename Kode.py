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

def detect_distro():
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("ID="):
                    return line.strip().split("=")[1].strip('"').lower()
    except Exception:
        return "unknown"
def neofetch_minimal():
    distro = detect_distro()
    # Minimal ASCII logos + colors per distro
    logos = {
        "arch": ("\033[94m" +  # blue
                 r"""
       /\    
      /  \   
     / /\ \  
    / ____ \ 
   /_/    \_\
    """ + "\033[0m"),
        "ubuntu": ("\033[91m" +  # orange/red
                   r"""
      _ _   
     | | |  
     | | |  
     |_|_|  
    """ + "\033[0m"),
        "fedora": ("\033[96m" +  # cyan
                   r"""
    __      
   / /__    
  /  '_ \   
 /_/\_\_\  
    """ + "\033[0m")
    }
    ascii_logo = logos.get(distro, "\033[92m[ Kode! Linux ]\033[0m")  # green default

    # We'll gather minimal info via shell commands (no full neofetch)
    try:
        # OS Name
        with open("/etc/os-release") as f:
            lines = f.read()
        import re
        os_name = re.search(r'^PRETTY_NAME="([^"]+)"', lines, re.MULTILINE)
        os_name = os_name.group(1) if os_name else distro.capitalize()

        # Kernel version
        kernel = subprocess.check_output(["uname", "-r"]).decode().strip()

        # CPU model (first line from /proc/cpuinfo)
        cpuinfo = subprocess.check_output(["grep", "model name", "/proc/cpuinfo"]).decode().split('\n')[0]
        cpu_model = cpuinfo.split(':')[1].strip() if ':' in cpuinfo else "Unknown CPU"

        # Total RAM (in MB)
        meminfo = subprocess.check_output(["grep", "MemTotal", "/proc/meminfo"]).decode()
        mem_mb = int(re.search(r'\d+', meminfo).group()) // 1024

    except Exception as e:
        os_name = distro.capitalize()
        kernel = "Unknown Kernel"
        cpu_model = "Unknown CPU"
        mem_mb = "Unknown RAM"

    clear()
    # Print minimal ascii + specs
    print(ascii_logo)
    print(f"OS: {os_name}")
    print(f"Kernel: {kernel}")
    print(f"CPU: {cpu_model}")
    print(f"RAM: {mem_mb} MB")


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

def notewriting():
    logoloader()
    while True:
        whattodo = input(">> ").lower().strip()
        if whattodo == "info":
            clear()
            help_text = """
Info Menu for Kode!
---------------------------
new     - Creates a new file
edit    - Edits a file
del     - Deletes a file
settings - Opens the settings
credits - Show the credits
info    - Shows this help menu
"""
            if os.name == "posix":  # Linux/macOS only
                help_text += "neofetch - Shows a minimal OS info screen with custom ASCII art\n"
            input(f"{help_text}\nPress Enter to continue: ")
            clear()
        elif whattodo == "neofetch" and os.name == "posix":
            clear()
            neofetch_minimal()
        elif whattodo == "exit":
            print("Exiting Kode!")
            sys.exit()
        else:
            print(f"Command '{whattodo}' not recognized. Type 'info' for help.")
            time.sleep(0.5)
            clear()

if __name__ == "__main__":
    try:
        signup()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
