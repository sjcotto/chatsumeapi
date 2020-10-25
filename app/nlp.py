from transformers import (
    pipeline,
    GPT2LMHeadModel,
    GPT2Tokenizer
)


class NLP:
    def __init__(self):
        self.gen_model = GPT2LMHeadModel.from_pretrained('gpt2')
        self.gen_tokenizer = GPT2Tokenizer.from_pretrained('gpt2') 
         
    def generate(self, prompt="The epistemelogical limit"):
        
        inputs = self.gen_tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
        prompt_length = len(self.gen_tokenizer.decode(inputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True))
        outputs = self.gen_model.generate(inputs, max_length=200, do_sample=True, top_p=0.95, top_k=60)
        generated = prompt + self.gen_tokenizer.decode(outputs[0])[prompt_length:]
        return generated

    def sentiments(self, text: str):
        nlp = pipeline("sentiment-analysis")
        result = nlp(text)[0]
        return f"label: {result['label']}, with score: {round(result['score'], 4)}"
        
    def summarization(self, text: str):
        summarization = pipeline("summarization")
        summary_text = summarization(text)[0]['summary_text']
        return summary_text

    def qarization(self, text: str):
        MODEL_LOC = "distilbert-base-uncased-distilled-squad"
        TOKENIZER_LOC = "distilbert-base-uncased-distilled-squad"
        qa = pipeline(
            "question-answering",
            model=MODEL_LOC,
            tokenizer=TOKENIZER_LOC
        )
        context = " ".join(["The incubation period is around 5 days (range: 4-7 days) with a maximum of 12-13 day"]*10)
        result_text = qa({"question": "incubation period?", "context": context})
        return result_text


