# NeptunAI RNN

NeptunAI on [huggingface.co](https://huggingface.co/neptun-org).  
Based on [RWKV-LM](https://github.com/BlinkDL/RWKV-LM/tree/main?tab=readme-ov-file).

## Fine Tuning

### Tokenize data

0. Install [pipx](https://pipx.pypa.io/stable/installation)

1. Install python-poetry

```bash
pipx install poetry
```

2. RUN

```bash
bash ./run/generate-training-data-binaries.sh
```

3. CHECK: `./NEPTUN/datasets/processed`

<details>
<summary>Legacy Instructions</summary>

1. Use `.jsonl` format for your data (see [rwkv-5-world](https://huggingface.co/BlinkDL/rwkv-5-world) for formats).

2. Use `./RWKV/FineTuning/make_data.py` to tokenize it into `bin` and `idx` using the world tokenizer, suitable for fine-tuning world models.

3. Rename the base checkpoint in the model folder to `rwkv-init.pth`, and change the training commands to use:

   **Models:**

   - 0.1B = --n_layer 12 --n_embd 768 --lr_init 3e-5
   - **0.4B = --n_layer 24 --n_embd 1024 --lr_init 2e-5**
   - 1.5B = --n_layer 24 --n_embd 2048 --lr_init 1.5e-5
   - 3B = --n_layer 32 --n_embd 2560 --lr_init 1e-5
   - 7B = --n_layer 32 --n_embd 4096 --vocab_size 65536 --lr_init 1e-5 --lr_final 1e-5

_Example_: `python3 make_data.py demo.jsonl 24 1024`

</details>

### About The Data

This repository is collection of scraped CSV & jsonl data from various sources used to train the neptun-ai. Below you can find a brief desciption of the used workflow, data-format & used tools.

#### Workflow

- Scrape Docker Documentation:
  - Extract tutorial content, including titles, headings, and detailed instructions.
  - Preserve the structure of the documentation (section headers and code snippets).
- Preprocess the Data:
  - Pair tutorial content with potential questions derived from the text.
  - Create a JSONL dataset for model training.
  - Follow the `demo.jsonl`-structure for the data structure
- Train RWKV:
  - Use the structured dataset to fine-tune the RWKV model for answering Docker questions.

#### Tools used for scraping and downloading

- CHATGPT GPT's
  - Scraper-GPT
  - Data Analyst-GPT

#### Conversation Description of `demo.jsonl`

#### What the User Wanted

- **Purpose**: The user tested how well the AI could edit, explain, and analyze text.
- **Tasks**: The user asked for things like fixing sentences, summarizing articles, solving technical problems, and understanding tricky meanings.

#### What the AI Did

- **Clear Answers**: The AI followed instructions and gave step-by-step responses.
- **Helpful Edits**: It fixed grammar, added spaces, and improved sentences with clear explanations.
- **Understood Context**: It figured out tricky phrases and cultural meanings correctly.
- **Solved Problems**: It used facts and logic to answer technical or scientific questions.

#### Takeaways

- The AI can follow detailed instructions well.
- It explains changes clearly and in simple terms.
- It adapts to different kinds of tasks and questions.

#### Data Description of `/data`

##### `get-started`

Uses the scrapped data from [Link](https://docs.docker.com/get-started/) and provides a data.jsonl for every page which is tagged in the navigation sidebar.
