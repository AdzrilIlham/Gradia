#!/bin/bash
# Script untuk menjalankan Gradia (Academic Performance Analytics)

cd "$(dirname "$0")"

if [ -d ".venv" ]; then
    echo "Menggunakan virtual environment (.venv)..."
    .venv/bin/python -m streamlit run app.py
else
    echo "Virtual environment tidak ditemukan, menjalankan dengan streamlit sistem..."
    streamlit run app.py
fi
