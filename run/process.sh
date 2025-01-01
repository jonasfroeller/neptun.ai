#!/bin/bash

RWKV_PATH="$(pwd)/RWKV"
PYTHON_SCRIPTS_PATH="$(pwd)/python-scripts"

cd "$RWKV_PATH"
pip install -r requirements.txt

cd "$PYTHON_SCRIPTS_PATH"
python process_data.py