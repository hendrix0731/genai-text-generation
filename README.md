
# Generative AI Text Generation using GPT-2

This project demonstrates text generation using a pretrained **GPT-2 model** from Hugging Face's `transformers` library. It takes a text prompt and generates new text using different temperature values.

---

##  Files

```
├── Question2.py              # Main script for text generation
├── generated_outputs.txt     # Output showing text samples with different temperatures
├── README.md                 # Project documentation
├── LICENSE                   # MIT License
├── requirements.txt          # Dependencies list
```

---

##  Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install transformers torch
```

---

##  How to Run

1. Run the script:

```bash
python Question2.py
```

2. Enter a text prompt when asked (e.g., `Once upon a time`).

3. The script generates text using two temperature values: **0.7** and **1.0**, using:
   - `top_k=50`
   - `max_new_tokens=50`

4. Outputs are saved in the file: `generated_outputs.txt`.

---

##  Example Output

```
=== Output with temperature=0.7 ===
Once upon a time ...

=== Output with temperature=1.0 ===
Once upon a time ...
```

You can open `generated_outputs.txt` to see the full outputs.

---

##  License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

##  Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [GPT-2 Model Card](https://huggingface.co/gpt2)
