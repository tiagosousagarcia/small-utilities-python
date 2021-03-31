#Example of text generation using GPT-2 model
#Guide at https://towardsdatascience.com/text-generation-with-python-and-gpt-2-1fecbff1635b

#See https://pytorch.org/
import torch
#See https://huggingface.co/transformers/index.html
from transformers import GPT2LMHeadModel, GPT2Tokenizer

#initialise tokeniser and model from pre-trained GPT2 model

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

#add input and tokenise it
prompt = 'She opened the cellar door.'
inputs = tokenizer.encode(prompt, return_tensors = 'pt')

#generate -- output is a series of indices
outputs = model.generate(inputs, max_length = 100, do_sample = True, temperature = .7, top_k = 50)

#decode indices into words
text = tokenizer.decode(outputs[0], skip_special_tokens = True)

#print result
print(text)