@echo off

:: Set paths relative to the current directory
set "RWKV_PATH=%CD%\..\..\RWKV"
set "PYTHON_SCRIPTS_PATH=%CD%\..\scripts"
set "TRAINING_DATA=%CD%\..\datasets\training-data.jsonl"

:: Change to the Python scripts directory
cd "%PYTHON_SCRIPTS_PATH%"

:: Install requirements using poetry
poetry run pip install -r "%RWKV_PATH%\requirements.txt"

:: Run make_data.py with the specified parameters (3 epochs, 4096 tokens of context)
poetry run python "%RWKV_PATH%\FineTuning\make_data.py" "%TRAINING_DATA%" 3 4096
