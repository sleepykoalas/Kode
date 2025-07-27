import os
import sys
import json
import time
import hashlib
import secrets
from getpass import getpass

def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        for _ in range(50):
            print()

def credits():
    print("""
╔════════════════════════════════════════════════════════════════════════╗
║                                CREDITS                                ║
╠════════════════════════════════════════════════════════════════════════╣
║  Project Title     : Kode!                                            ║
║  Description       : A custom-developed software solution created by  ║
║                      Koala, designed for responsible and efficient    ║
║                      system usage in open computing environments.     ║
║                                                                        ║
║  Developed By      : Koala                                            ║
║                      Lead Developer & Software Architect              ║
║                                                                        ║
║  Platform Target   : Linux-Based Operating Systems                    ║
║                      (e.g., Ubuntu, Fedora, Arch, and other UNIX-like)║
║                                                                        ║
║  Primary Language  : Python                                           ║
║                                                                        ║
║  Repository        : Kode                                             ║
║                                                                        ║
║  License           : Open Source License (Custom Terms Apply)        ║
║                      Redistribution and modification are permitted    ║
║                      under author-defined conditions.                 ║
║                                                                        ║
║  Special Acknowledgments:                                             ║
║      - The Linux Foundation, for stewarding open-source innovation    ║
║      - The Free Software Community, for fostering ethical coding      ║
║      - Contributors and testers who provided vital feedback           ║
║                                                                        ║
║  Legal Notice:                                                        ║
║      This software is provided "as is", without any warranties.       ║
║      Usage is at the discretion of the end user and must comply       ║
║      with local regulations and project licensing terms.              ║
╚════════════════════════════════════════════════════════════════════════╝
""")

def hasher(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

def notetaker():
    clear()
    whattodo = input(">> ").lower().strip()
    if whattodo == "n":
        filegod("n")
    elif whattodo == "d":
        filegod("d")

def filegod(input_string):
    global username
    if input_string == "n":
        clear()
        new_file_name = input("Please Enter a file name: ")
        os.makedirs(f"Logs and Data/{username}", exist_ok=True)
        filepath = os.path.join(username, new_file_name)
        if os.path.exists(filepath):
            print("This file exists already! Please choose another one!")
            time.sleep(1)
            return
        if "." in new_file_name and not new_file_name.startswith("."):
            ext = new_file_name.rsplit(".", 1)[-1]
            filename = new_file_name
            print("Creating...")
            with open(filepath, "w") as f:
                f.write("")
        else:
            ext = False
            filename = new_file_name+".txt"
            print("Creating...")
            with open(filepath, "w") as f:
                f.write("")
        clear()
        input("The file has been created! Please click Enter to continue: ")
        notetaker()

def newpassword():
    new_backup_code = secrets.token_hex(8)
    while True:
        new_code = input(f"Code Correct! Here's a new code {new_backup_code}! Type GOT IT to continue: ")
        if new_code.strip() == "GOT IT":
            with open("Logs and Data/users.json", "r") as f:
                data = json.load(f)
            data["backup_code"] = hasher(new_backup_code)
            with open("Logs and Data/users.json", "w") as f:
                json.dump(data, f, indent=4, sort_keys=True)
            clear()
            new_password_user = getpass("Please Enter your new Password: ")
            con_password_user = getpass("Please comfirm your Password: ")
            if new_password_user == con_password_user:
                if len(con_password_user) < 8:
                    len_password = input("Your password is not secure! Are you sure you would like to continue (Y/n)? ").lower().strip()
                    if "n" in len_password:
                        newpassword()
                    else:
                        notetaker()
                        break
                else:
                    notetaker()
                    break
            else:
                print("Passwords do not match! Try again.")
                time.sleep(1)
                newpassword()

def backupcode():
    while True:
        clear()
        backup_code = secrets.token_hex(8)
        backup_imform = input(f"Thanks for using Kode! {username}! Your account password recovery code is: {backup_code}. Type I'M DONE to continue: ")
        if backup_imform.strip() == "I'M DONE":
            data = {
                "username": hasher(username),
                "password": hasher(password),
                "backup_code": hasher(backup_code)
            }
            os.makedirs("Logs and Data", exist_ok=True)
            with open("Logs and Data/users.json", "w") as f:
                json.dump(data, f, indent=4, sort_keys=True)
            notetaker()
            break

def signup():
    global username
    global password
    clear()
    username = input("Welcome to Kode! Please Enter a username: ")
    password = getpass(f"Please Enter a password {username}! ")
    if len(password) < 8:
        password_continue = input("Your password is not secure! Are you sure you would like to continue (Y/n)? ").lower().strip()
        if "n" in password_continue:
            signup()
        else:
            backupcode()
    else:
        backupcode()

def login():
    lo_username = input("Welcome back to Kode! Please Enter a username: ")
    lo_password = getpass("Please Enter a password (Type 'recov' for password recovery): ").lower()

    with open("Logs and Data/users.json", "r") as f:
        data = json.load(f)

    if lo_password == "recov":
        while True:
            clear()
            password_recov = input("Please Enter your recovery code: ")
            if hasher(password_recov) == data["backup_code"]:
                newpassword()
                break
            else:
                print("Your code does not match! Please try again!")
                time.sleep(1)
    else:
        if hasher(lo_password) == data["password"]:
            notetaker()
        else:
            print("Wrong Password!")
            time.sleep(0.5)
            login()

def main():
    try:
        if not os.path.exists("Logs and Data/users.json"):
            clear()
            signup()
        else:
            clear()
            login()
    except KeyboardInterrupt:
        clear()
        print("Exiting...")
        sys.exit()
    credits()
    input("")
    notetaker()

if __name__ == "__main__":
    main()
