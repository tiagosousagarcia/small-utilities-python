def generate_text(prompt, nr_words):
    inputs = tokenizer.encode(prompt, return_tensors = 'pt')
    outputs = model.generate(inputs, max_length = nr_words, do_sample = True, temperature = .7, top_k = 50)
    text = tokenizer.decode(outputs[0], skip_special_tokens = True)
    print("\n")
    print(text)
    print("\n\n")
    return text

def generate_more(current_text):
    prompt = current_text
    current_words = len(prompt.split())
    nr_words = current_words + round(current_words*0.5)
    current_text = generate_text(prompt, nr_words)
    return current_text

def exit_program(current_text):
    option = input("\nDo you want to save your story? (y/n): ")
    if option == "n":
        print("\nIt was fun writing with you, come back soon!")
    elif option == "y":
        print("\nLet's save that story!")
        now = datetime.now()
        date_string = now.strftime("%Y%m%d%H%M")
        file_name = date_string + "_story.txt"
        if not os.path.isdir("./stories/"):
            os.mkdir("./stories/")
        final_file = open(os.path.join("./stories/", file_name), "w")
        final_file.write(current_text)
        final_file.close()
        print("\nYour story was saved with the name ", file_name)
        print("\nIt was fun writing with you, come back soon!")
    else:
        print("\nI'm sorry, I didn't get that")
        exit_program(current_text)
    return 0



def main_menu(current_text):
    print("\t\t==============MAIN MENU==============\n")
    print("1 - Ask the wizard to write some more")
    print("2 - Write some more on your own")
    print("3 - Read what you have so far")
    print("4 - You are finished with writing")
    option = input("\nWhat should we do next? (Choose a number): ")
    if option == "1":
        new_text = generate_more(current_text)
        main_menu(new_text)
    elif option == "2":
        more_text = input("\nHow should the story continue?\n")
        current_text = current_text + more_text
        main_menu(current_text)
    elif option == "3":
        print("\n")
        print(current_text)
        print("\n")
        main_menu(current_text)
    elif option == "4":
        exit_program(current_text)
    else:
        print("\nI'm sorry, that is not a valid option")
        main_menu(current_text)
    return 0


#initialization
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from datetime import datetime
import os
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

#first run
prompt = input("How should we start our story?\n")
nr_words = 2 * len(prompt.split())
current_text = generate_text(prompt, nr_words)
main_menu(current_text)