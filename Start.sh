#!/bin/sh

if command -v python &>/dev/null; then
    echo "Python is installed. Running Meta.py..."
    python Meta.py
else
    echo "Python is required to run Meta.py. Please install Python."
fi
