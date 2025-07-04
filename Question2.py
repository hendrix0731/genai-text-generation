from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch


# GPT-2 model and tokenizer from Hugging Face 
model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Set device (GPU if available, else CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

# prompt taken from users
prompt = input("Enter a text prompt: ")
input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)

# Generation setting
max_tokens = 50
top_k = 50
temperatures = [0.7, 1.0]

# Store outputs
outputs = {}

# Generate text for different temperature
for temp in temperatures:
    output = model.generate(
        input_ids,
        do_sample=True,
        max_new_tokens=max_tokens,
        top_k=top_k,
        temperature=temp
    )
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    outputs[temp] = generated_text

# Save results to a outputfile
with open("generated_outputs.txt", "w", encoding="utf-8") as f:
    for temp, text in outputs.items():
        f.write(f"=== Output with temperature={temp} ===\n")
        f.write(text + "\n\n")

print("\n✅ Text generation complete. Outputs saved in 'generated_outputs.txt'.")
