# Neptun AI

## Fine Tuning

1. Use `.jsonl` format for your data (see https://huggingface.co/BlinkDL/rwkv-5-world for formats).

2. Use `./RWKV/FineTuning/make_data.py` to tokenize it into `binidx` using the world tokenizer, suitable for fine-tuning World models.

3. Rename the base checkpoint in the model folder to `rwkv-init.pth`, and change the training commands to use `--n_layer 32 --n_embd 4096 --vocab_size 65536 --lr_init 1e-5 --lr_final 1e-5` for 7B.

   **Models:**

   - 0.1B = --n_layer 12 --n_embd 768
   - **0.4B = --n_layer 24 --n_embd 1024**
   - 1.5B = --n_layer 24 --n_embd 2048
   - 3B = --n_layer 32 --n_embd 2560
   - 7B = --n_layer 32 --n_embd 4096

Example: `python3 make_data.py demo.jsonl 24 1024`
