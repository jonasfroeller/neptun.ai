import json
from pathlib import Path
import shutil

def combine_jsonl_files(input_dir, output_file):
    """
    Combines all JSONL files from the input directory into a single output file.
    Validates JSON format and creates a backup of existing output file.
    
    Args:
        input_dir (str): Path to directory containing JSONL files
        output_file (str): Path to output file
    """
    input_path = Path(input_dir)
    output_path = Path(output_file)
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    if output_path.exists():
        backup_path = output_path.with_suffix('.jsonl.bak')
        shutil.copy2(output_path, backup_path)
        print(f"Created backup: {backup_path}")
    
    processed_files = 0
    total_lines = 0
    
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for jsonl_file in input_path.glob('**/*.jsonl'):
            try:
                with open(jsonl_file, 'r', encoding='utf-8') as infile:
                    for line in infile:
                        try:
                            json.loads(line.strip())
                            outfile.write(line)
                            total_lines += 1
                        except json.JSONDecodeError:
                            print(f"Skipping invalid JSON line in {jsonl_file}")
                            continue
                processed_files += 1
                print(f"Processed: {jsonl_file}")
            except Exception as e:
                print(f"Error processing {jsonl_file}: {e}")
    
    print(f"\nSummary:")
    print(f"Processed files: {processed_files}")
    print(f"Total lines: {total_lines}")
    print(f"Combined file saved to: {output_path}")

if __name__ == "__main__":
    JSONL_DIR = Path("../datasets/jsonl")
    OUTPUT_FILE = Path("../datasets/training-data.jsonl")
    
    combine_jsonl_files(JSONL_DIR, OUTPUT_FILE)
