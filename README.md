# Neptun AI

NeptunAI on [huggingface.co](https://huggingface.co/neptun-org).  
Based on [RWKV-LM](https://github.com/BlinkDL/RWKV-LM/tree/main?tab=readme-ov-file).

## Fine Tuning

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
