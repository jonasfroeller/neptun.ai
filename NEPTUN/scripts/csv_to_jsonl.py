import pandas as pd
import json
import os
from pathlib import Path

def convert_csv_to_jsonl(csv_path, output_path):
    # Process CSV in chunks to minimize memory usage
    chunk_size = 1000
    chunks = pd.read_csv(csv_path, chunksize=chunk_size)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for chunk in chunks:
            for _, row in chunk.iterrows():
                formatted_text = (
                    f"System: You are a helpful Docker expert.\n\n"
                    f"User: {row['prompt']}\n\n"
                    f"Assistant: {row['response']}"
                )
                json_obj = {"text": formatted_text}
                f.write(json.dumps(json_obj, ensure_ascii=False) + '\n')

def process_directory():
    csv_dir = Path("../datasets/raw/csv")
    jsonl_dir = Path("../datasets/jsonl")
    
    for csv_file in csv_dir.glob("*.csv"):
        output_file = jsonl_dir / f"{csv_file.stem}.jsonl"
        print(f"Converting {csv_file} to {output_file}")
        convert_csv_to_jsonl(str(csv_file), str(output_file))
        print(f"Conversion completed: {output_file}")

if __name__ == "__main__":
    process_directory()
