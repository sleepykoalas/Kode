#!/bin/bash

clear

# Move to the directory where this script lives
cd "$(dirname "$0")"

python3 Kode.py

echo ""
read -p "Press Enter to continue..." dummy_var
