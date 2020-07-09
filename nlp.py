from transformers import (
    GPT2LMHeadModel,
    GPT2Tokenizer,
    pipeline,
    AutoModelWithLMHead,
    AutoTokenizer
)
import torch
import re


class NLP:
    def __init__(self):
        
        self.gen_model = GPT2LMHeadModel.from_pretrained('gpt2')
        self.gen_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')  # Add specific options if needed
        self.generated = None
        self.chat_tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        self.chat_model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-medium")


    def generate(self, PADDING_TEXT="BURN IT DOWN", prompt="I do no not see why"):
        
        inputs = self.gen_tokenizer.encode(PADDING_TEXT + prompt, add_special_tokens=False, return_tensors="pt")
        prompt_length = len(self.gen_tokenizer.decode(inputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True))
        outputs = self.gen_model .generate(inputs, max_length=250, do_sample=True, top_p=0.95, top_k=60)
        generated = prompt + self.gen_tokenizer.decode(outputs[0])[prompt_length:]

    def ner(self, sentence):

        nlp = pipeline("ner")
        return nlp(sentence)

    def chat_bot(self):
        tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        model = AutoModelWithLMHead.from_pretrained("microsoft/DialoGPT-medium")
        # Let's chat for 5 lines
        for step in range(5):
            # encode the new user input, add the eos_token and return a tensor in Pytorch
            new_user_input_ids = tokenizer.encode(input(">> User:") + tokenizer.eos_token, return_tensors='pt')

            # append the new user input tokens to the chat history
            bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

            # generated a response while limiting the total chat history to 1000 tokens, 
            chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

            # pretty print last ouput tokens from bot
            print("DialoGPT: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))

    def sentiments(self):
        return "SA"

    