from transformers import (
    pipeline,
    AutoModelWithLMHead,
    AutoTokenizer,
    AutoModelForTokenClassification
)
import torch
import re


class NLP:
    def __init__(self):
        self.gen_model = AutoModelForCausalLM.from_pretrained('gpt2')
        self.gen_tokenizer = AutoTokenizer.from_pretrained('gpt2')  # Add specific options if needed
        self.chat_tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        self.chat_model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
        self.ner_model = AutoModelForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
        self.ner_tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
    
    def generate(self, PADDING_TEXT="...", prompt="The epistemelogical limit"):
        
        inputs = self.gen_tokenizer.encode(PADDING_TEXT + prompt, add_special_tokens=False, return_tensors="pt")
        prompt_length = len(self.gen_tokenizer.decode(inputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True))
        outputs = self.gen_model .generate(inputs, max_length=200, do_sample=True, top_p=0.95, top_k=60)
        generated = prompt + self.gen_tokenizer.decode(outputs[0])[prompt_length:]
        return str("generated")

    def ner(self, text: str):

        label_list = [
            " O ",       # Outside of a named entity
            " B-MISC ",  # Beginning of a miscellaneous entity right after another miscellaneous entity
            " I-MISC ",  # Miscellaneous entity
            " B-PER ",   # Beginning of a person's name right after another person's name
            " I-PER ",   # Person's name
            " B-ORG ",   # Beginning of an organisation right after another organisation
            " I-ORG ",   # Organisation
            " B-LOC ",   # Beginning of a location right after another location
            " I-LOC "    # Location
        ]
        # Bit of a hack to get the tokens with the special tokens
        tokens = self.ner_tokenizer.tokenize(self.ner_tokenizer.decode(self.ner_tokenizer.encode(text)))
        inputs = self.ner_tokenizer.encode(text, return_tensors="pt")
        outputs = self.ner_model(inputs)[0]
        predictions = torch.argmax(outputs, dim=2)

        pred = [[token, label_list[prediction]] for token, prediction in zip(tokens, predictions[0].numpy())]

        for v in pred:
            for i, j in enumerate(pred):
                if j[1] is " O ":
                    del pred[i]      
        return pred

    def chat_bot(self, text: str):
        # Let's chat for 5 lines
        for step in range(1):
            # encode the new user input, add the eos_token and return a tensor in Pytorch
            new_user_input_ids = self.chat_tokenizer.encode(text + self.chat_tokenizer.eos_token, return_tensors='pt')

            # append the new user input tokens to the chat history
            bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

            # generated a response while limiting the total chat history to 1000 tokens, 
            chat_history_ids = self.chat_model.generate(bot_input_ids, max_length=1000, pad_token_id=self.chat_tokenizer.eos_token_id)

            # pretty print last ouput tokens from bot
            return f" {self.chat_tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)}"

    def sentiments(self, text: str):
        nlp = pipeline("sentiment-analysis")
        result = nlp(text)[0]
        return f"label: {result['label']}, with score: {round(result['score'], 4)}"

    