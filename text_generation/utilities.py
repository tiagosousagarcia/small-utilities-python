import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

def generate_text(prompt, nr_words):
    inputs = tokenizer.encode(prompt, return_tensors = 'pt')
    outputs = model.generate(inputs, max_length = nr_words, do_sample = True, temperature = .7, top_k = 50)
    text = tokenizer.decode(outputs[0], skip_special_tokens = True)
    return text