#!/bin/bash

RWKV_PATH="$(pwd)/../../RWKV"
PYTHON_SCRIPTS_PATH="$(pwd)/../scripts"
TRAINING_DATA="$(pwd)/../datasets/training-data.jsonl"

cd "$PYTHON_SCRIPTS_PATH"

# Use poetry run to execute the commands within the poetry environment
poetry run pip install -r "$RWKV_PATH/requirements.txt"

# Run make_data.py directly with the specific file (3 epochs, 4096 tokens of context)
poetry run python "$RWKV_PATH/FineTuning/make_data.py" "$TRAINING_DATA" 3 4096
