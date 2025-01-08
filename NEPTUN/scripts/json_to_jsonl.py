import json
from pathlib import Path

def convert_json_to_jsonl(json_path, output_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for item in data:
            formatted_text = (
                f"System: {item['instruction']}\n\n"
                f"User: {item['input']}\n\n"
                f"Assistant: {item['output']}"
            )
            json_obj = {"text": formatted_text}
            f.write(json.dumps(json_obj, ensure_ascii=False) + '\n')

def process_directory():
    json_dir = Path("../datasets/raw/json")
    jsonl_dir = Path("../datasets/jsonl")
    
    for json_file in json_dir.glob("*.json"):
        output_file = jsonl_dir / f"{json_file.stem}.jsonl"
        print(f"Converting {json_file} to {output_file}")
        convert_json_to_jsonl(str(json_file), str(output_file))
        print(f"Conversion completed: {output_file}")

if __name__ == "__main__":
    process_directory()
