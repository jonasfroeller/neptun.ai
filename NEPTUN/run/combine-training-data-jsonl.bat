@echo off

set SCRIPT_DIR=%~dp0
set PROJECT_ROOT=%SCRIPT_DIR%..\scripts

cd /d "%PROJECT_ROOT%"

poetry run python combine_jsonl.py

pause
