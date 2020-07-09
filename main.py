from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from train import bot
from pydantic import BaseModel


class Item(BaseModel):
    mssg: str

app = FastAPI()

origins = [

    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/chat/")
async def bot_mssg(item: Item):
    print(item.mssg)
    # response = bot.get_response(msg)
    # print("Res", response)
    return item.mssg

@app.get("/ner/")
async def  named_entity_recognition():
    return {"ner": "NER"}