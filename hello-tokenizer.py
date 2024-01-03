from transformers import AutoModelForCausalLM, AutoTokenizer

# !!! Warning: Running this code for the first time will download about 18GB of data to your system
# !!! On a Mac it is stored in /Users/username/.cache/huggingface

model_name = "HuggingFaceH4/zephyr-7b-alpha"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

input_text = ("Python code to generate tic-tac-toe")  # Change the prompt here
input_ids = tokenizer.encode(input_text, return_tensors='pt')
output = model.generate(input_ids, max_length=1000)  # Change max_length to a lower number for faster responses.
response = tokenizer.decode(output[0],  skip_special_tokens=True)
print(response)