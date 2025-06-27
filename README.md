# Kode!

Kode! is a lightweight, text-based editor implemented in Python. It emphasizes security and privacy by hashing user credentials and providing a one-time recovery code for account backup.

## Features

- Simple and efficient text-based interface  
- Secure user signup with SHA-256 hashed usernames and passwords  
- Generates a unique recovery code displayed only once per user  
- Cross-platform support for clearing the console screen (Windows, Linux, macOS)  
- Hidden password input using the `getpass` module  

## Requirements

- Python 3.6 or higher  
- No external dependencies required; utilizes Python's standard library  

## Usage

1. Download or clone the repository.  
2. Run the main script using the command:  
   ```bash
   python kode.py

    Follow the on-screen prompts to create a user account, enter a secure password, and receive a recovery code.

Implementation Details

    The program securely hashes usernames and passwords with SHA-256 before storage or processing.

    A unique recovery code is generated per signup for password recovery purposes and is shown only once.

    The console screen is cleared appropriately depending on the detected operating system to maintain a clean user interface.

    Users with passwords shorter than eight characters receive a warning and must confirm their choice.

Limitations & Future Work

    Currently, the program supports single-user signup with no persistent storage.

    Multi-user support, encrypted storage, and enhanced text editing features are planned for future versions.

License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.

P.S: Those on Linux (only Linux, no UNIX), theres a surprise :)
