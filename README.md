# Kode!

Kode! is a minimalistic and secure terminal-based note-taking application designed primarily for Linux users. It provides a simple, privacy-focused interface for managing notes, with hashed credential storage and a clean command-line experience.

---

## Features

- Secure user signup with hashed usernames and passwords  
- Create, delete, and manage note files stored in user-specific directories  
- Clear and intuitive terminal interface  
- Backup codes for password recovery  
- Cross-platform support with scripts for Linux/macOS and Windows  

---

## Installation

1. Clone or download the repository.  
2. Ensure Python 3 is installed on your system.  
3. (Optional) On Linux/macOS, make the launch script executable:  
   ```bash
   chmod +x run_kode.sh

    Run the application:

        Linux:

./run_kode.sh

macOS:
It is recommended to run the Python script directly:

python3 Kode.py

If running the Python script directly does not work, you may use the provided shell script as an alternative:

./run_kode.sh

Windows:
It is recommended to run the application directly using Python via the command prompt:

        python Kode.py

        However, if running Python directly is problematic, you may use the provided run_kode.bat batch script as an alternative to launch the application.

Usage

    At the prompt, enter one of the following commands:

        new — Create a new note file

        del — Delete an existing note file

        info — Display the help menu

        exit — Exit the application

    User credentials and backup codes are securely hashed.

    Notes are saved as randomly named .txt files within the Logs and Data/<username>/ directory.

Secret Linux Feature

Linux users can discover a hidden command that displays minimal system information with custom ASCII art. This command is not listed in the help menu but can be accessed by typing:

neofetch

Try it out if you’re feeling adventurous! 🐧✨
Contributing

Contributions are welcome! Please submit issues or pull requests to enhance functionality or fix bugs. Preference is given to Linux-compatible improvements.
License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.
Disclaimer

Kode! is designed with a Linux-first philosophy. While Windows support is provided via batch scripts, full functionality and optimal experience are achieved on Linux systems.
