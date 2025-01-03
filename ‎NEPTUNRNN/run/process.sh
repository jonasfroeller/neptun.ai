#!/bin/bash

RWKV_PATH="$(pwd)/../../RWKV"
PYTHON_SCRIPTS_PATH="$(pwd)/../python-scripts"

cd "$PYTHON_SCRIPTS_PATH"

# Use poetry run to execute the commands within the poetry environment
poetry run pip install -r "$RWKV_PATH/requirements.txt"

# Run the Python script with poetry
poetry run python process_data.py
