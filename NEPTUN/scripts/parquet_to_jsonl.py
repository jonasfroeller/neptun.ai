#!/usr/bin/env python3
import json
import logging
import pandas as pd
from pathlib import Path
from typing import Union, Dict, Any

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('parquet_to_jsonl.log'),
        logging.StreamHandler()
    ]
)

def process_row(row: Dict[str, Any]) -> Dict[str, Any]:
    """Process a single row of data to ensure it matches our JSONL format."""
    # Convert row to dict if it's a pandas Series
    if isinstance(row, pd.Series):
        row = row.to_dict()
    
    # Remove any None/NaN values
    row = {k: v for k, v in row.items() if pd.notna(v)}
    
    input_text = (
        row.get('instruction', '') or 
        row.get('question', '') or 
        row.get('query', '') or 
        row.get('prompt', '') or
        row.get('input', '') or
        ''
    )
    
    output_text = (
        row.get('answer', '') or 
        row.get('response', '') or 
        row.get('output', '') or 
        ''
    )
    
    formatted_text = (
        f"System: You are a helpful Docker expert.\n\n"
        f"User: {input_text}\n\n"
        f"Assistant: {output_text}"
    )
    
    return {"text": formatted_text}

def convert_parquet_to_jsonl(
    input_file: Union[str, Path],
    output_file: Union[str, Path]
) -> None:
    """
    Convert a parquet file to JSONL format.
    
    Args:
        input_file: Path to the input parquet file
        output_file: Path where the JSONL file will be saved
    """
    try:
        logging.info(f"Reading parquet file: {input_file}")
        df = pd.read_parquet(input_file)
        
        logging.info(f"Converting to JSONL and writing to: {output_file}")
        with open(output_file, 'w', encoding='utf-8') as f:
            for _, row in df.iterrows():
                processed_row = process_row(row)
                if processed_row:  # Only write if we have data
                    f.write(json.dumps(processed_row, ensure_ascii=False) + '\n')
        
        logging.info(f"Successfully converted {input_file} to {output_file}")
        
    except Exception as e:
        logging.error(f"Error processing {input_file}: {str(e)}")
        raise

def main():
    parquet_dir = Path("../datasets/raw/parquet")
    jsonl_dir = Path("../datasets/jsonl")
    
    jsonl_dir.mkdir(parents=True, exist_ok=True)
    
    for parquet_file in parquet_dir.glob("*.parquet"):
        output_file = jsonl_dir / f"{parquet_file.stem}.jsonl"
        logging.info(f"Processing {parquet_file.name}")
        convert_parquet_to_jsonl(parquet_file, output_file)

if __name__ == "__main__":
    try:
        main()
        logging.info("All files processed successfully")
    except Exception as e:
        logging.error(f"Script failed: {str(e)}")
        raise
