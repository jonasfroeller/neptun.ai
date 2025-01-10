#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$SCRIPT_DIR/../scripts"

cd "$PROJECT_ROOT"

poetry run python combine_jsonl.py
