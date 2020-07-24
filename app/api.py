from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.train import bot
from pydantic import BaseModel
# from nlp import NLP

class Message(BaseModel):
    input: str
    output: str = None

app = FastAPI()
# nlp = NLP()

origins = [
    "https://www.metavisuo.com/nlp",
    "https://www.metavisuo.com",
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST","GET"],
    allow_headers=["*"],
)

@app.post("/chat/")
async def chat_chatterbot(message: Message):
<<<<<<< HEAD
    message.output  = str(bot.get_response(message.input))
    return {"output" : message.output}

@app.post("/sentiment/")
async def sentiment_analysis(message: Message):
    message.output  = str(nlp.sentiments(message.input))
    return {"output" : message.output}

@app.post("/ner/")
async def  named_entity_recognition(message: Message):
    if not message.input:
        return
    print("NER", nlp.ner(message.input))
    return {"output" : nlp.ner(message.input)}

@app.post("/generative/")
async def  generate(message: Message):
    message.output  = nlp.generate(prompt=message.input)
    return {"output" : message.output}

@app.post("/chat_dialo/")
async def  chat_dialo(message: Message):
    message.output  = nlp.chat_bot(message.input)
    return {"output" : message.output}
=======
    # message.output  = str(bot.get_response(message.input))
    return {"output" : "BENNY A GOOD DUDE"}



# @app.post("/sentiment/")
# async def sentiment_analysis(message: Message):
#     message.output  = str(nlp.sentiments(message.input))
#     return {"output" : message.output}

# @app.post("/ner/")
# async def  named_entity_recognition(message: Message):
#     if not message.input:
#         return
#     print("NER", nlp.ner(message.input))
#     return {"output" : nlp.ner(message.input)}

# @app.post("/generative/")
# async def  generate(message: Message):
#     message.output  = nlp.generate()
#     return {"output" : message.output}

# @app.post("/chat_dialo/")
# async def  chat_dialo(message: Message):
#     message.output  = nlp.chat_bot(message.input)
#     return {"output" : message.output}
>>>>>>> production_deployment
