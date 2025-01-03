import os
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../datasets"))
PROCESSED_DIR = os.path.join(BASE_DIR, "processed")
MAKE_DATA_SCRIPT = os.path.abspath(os.path.join(SCRIPT_DIR, "../../RWKV/FineTuning/make_data.py"))
CTX_LEN = 4096
EPOCHS = 3

def find_jsonl_files(base_dir):
    """Recursively find all .jsonl files in the given directory."""
    jsonl_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".jsonl"):
                jsonl_files.append(os.path.join(root, file))
    return jsonl_files

def is_file_empty(file_path):
    """Check if a file is empty."""
    return os.path.getsize(file_path) == 0

def process_file(file_path):
    """Run the make_data.py script for a single .jsonl file."""
    if is_file_empty(file_path):
        print(f"Skipping empty file: {file_path}")
        return

    output_name = os.path.splitext(os.path.basename(file_path))[0]
    print(f"Processing: {file_path} -> Output: {output_name}.bin/.idx")
    
    command = [
        "python3", MAKE_DATA_SCRIPT,
        file_path, str(EPOCHS), str(CTX_LEN)
    ]
    
    # Run the make_data.py script
    try:
        subprocess.run(command, check=True)
        print(f"Successfully processed: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {file_path}: {e}")

def main():
    jsonl_files = find_jsonl_files(BASE_DIR)
    
    if not jsonl_files:
        print("No .jsonl files found in the data directory.")
        return

    for jsonl_file in jsonl_files:
        process_file(jsonl_file)

if __name__ == "__main__":
    main()
