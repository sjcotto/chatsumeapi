from fastapi import FastAPI


# nlp = NLP()
app = FastAPI()
from train import bot


@app.post("/chat/")
async def get_bot_response(msg: str):    
    # response = bot.get_response(data["mssg"])
    return {"chat": msg}

@app.get("/ner/")
async def  named_entity_recognition():
    return {"ner": "NER"}

if __name__ == "__main__":    
    app.run(host ='0.0.0.0', port = 5001, debug = True)
