
# Kode!

**Kode!** is a minimalist, text-based editor built in Python with a focus on simplicity, speed, and security. Designed for terminal environments, Kode! provides a lightweight and distraction-free writing experience with built-in account and backup systems.

---

## Features

- Command-line interface (CLI) for fast and simple text editing  
- Secure account setup with SHA-256 password hashing  
- One-time recovery code for password reset support  
- Intelligent OS detection with appropriate screen clearing behavior  
- User-friendly navigation and visual branding through ASCII art  

---

## Installation

### Requirements

- Python 3.7 or newer  
- No external libraries required; uses only the Python standard library  

### Setup

Clone the repository and run the program:

```bash
git clone https://github.com/YOUR-USERNAME/kode.git
cd kode
python3 kode.py
````

> **Note:** Kode! is optimized for Linux, macOS, and WSL environments. It may not perform as expected on native Windows terminals.

---

## Usage

Once launched, follow the on-screen prompts to:

* Create a new username and password
* Receive a one-time backup recovery code
* Access the Kode! editor shell

From the main menu, you can:

* Create new files
* Edit existing files
* Delete files
* Access application settings
* View credits
* Read the help/info section

---

## Data Storage

User data is stored in a local JSON file under:

```
Logs and Data/users.json
```

This file contains SHA-256 hashes of the username, password, and backup code. No plaintext information is stored.

---

## License

This project is licensed under the [Apache License 2.0](LICENSE).

---

## Acknowledgments

Kode! was created as a lightweight alternative for users seeking a secure, terminal-based environment.

---

**Made with 💻 and rage.**
