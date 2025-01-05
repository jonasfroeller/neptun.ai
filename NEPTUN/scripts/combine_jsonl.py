import json
from pathlib import Path
import shutil
import logging

# Configure logging to file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('combine_jsonl.log'),
        logging.StreamHandler()
    ]
)

def split_json_objects(line):
    """
    Splits a string containing multiple JSON objects into individual objects.
    
    Args:
        line (str): String potentially containing multiple JSON objects
    Returns:
        list: List of valid JSON strings
    """
    line = line.strip()
    if not line:
        return []
    
    # Try parsing as single JSON object first
    try:
        json.loads(line)
        return [line]
    except json.JSONDecodeError:
        pass
    
    # Handle multiple JSON objects
    json_objects = []
    current_object = ""
    bracket_count = 0
    
    for char in line:
        current_object += char
        if char == '{':
            bracket_count += 1
        elif char == '}':
            bracket_count -= 1
            
            if bracket_count == 0:
                try:
                    json.loads(current_object)
                    json_objects.append(current_object)
                    current_object = ""
                except json.JSONDecodeError:
                    logging.warning(f"Invalid JSON object found: {current_object}")
    
    return json_objects

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
        logging.info(f"Created backup: {backup_path}")
    
    processed_files = 0
    total_lines = 0
    problem_lines = 0
    
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for jsonl_file in input_path.glob('**/*.jsonl'):
            try:
                with open(jsonl_file, 'r', encoding='utf-8') as infile:
                    for line_num, line in enumerate(infile, 1):
                        json_objects = split_json_objects(line)
                        
                        if not json_objects:
                            problem_lines += 1
                            logging.warning(f"Problem in line {line_num} of {jsonl_file} - Skipped")
                            continue
                        
                        for json_obj in json_objects:
                            outfile.write(json_obj + '\n')
                            total_lines += 1
                
                processed_files += 1
                logging.info(f"Processed: {jsonl_file}")
            except Exception as e:
                logging.error(f"Error processing {jsonl_file}: {e}")
    
    logging.info(f"\nSummary:")
    logging.info(f"Processed files: {processed_files}")
    logging.info(f"Total lines: {total_lines}")
    logging.info(f"Problem lines: {problem_lines}")
    logging.info(f"Combined file saved to: {output_path}")

if __name__ == "__main__":
    JSONL_DIR = Path("../datasets/jsonl")
    OUTPUT_FILE = Path("../datasets/training-data.jsonl")
    
    combine_jsonl_files(JSONL_DIR, OUTPUT_FILE)
