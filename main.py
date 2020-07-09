from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from train import bot
from pydantic import BaseModel
from nlp import NLP

class Message(BaseModel):
    input: str
    output: str = None

app = FastAPI()
nlp = NLP()

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
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/chat/")
async def bot_mssg(message: Message):
    message.output  = str(bot.get_response(message.input))
    return {"output" : message.output}

@app.get("/ner/")
async def  named_entity_recognition():
    return {"ner": "NER"}