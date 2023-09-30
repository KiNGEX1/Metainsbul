#!/bin/sh

if command -v python &>/dev/null; then
    echo "Python is installed. Running Metainsbul..."
    python Meta.py
else
    echo "Python is required to run Metainsbul Please install Python."
fi
