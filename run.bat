@echo off
title Gradia - Academic Performance Analytics
cd /d "%~dp0"

if exist ".venv\Scripts\activate.bat" (
    echo [INFO] Menggunakan virtual environment (.venv)...
    call .venv\Scripts\activate.bat
    python -m streamlit run app.py
) else (
    echo [INFO] Virtual environment tidak ditemukan, menjalankan dengan python/streamlit sistem...
    streamlit run app.py
)
pause
