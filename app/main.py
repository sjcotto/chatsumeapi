from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.nlp import NLP

class Message(BaseModel):
    input: str
    output: str = None

class QA(BaseModel):
    question: str
    context: str = None
    output: str = None

app = FastAPI()
nlp = NLP()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://search.kognitive.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST","GET"],
    allow_headers=["*"],
)

@app.post("/generative/")
async def  generate(message: Message):
    message.output  = nlp.generate(prompt=message.input)
    return {"output" : message.output}

@app.post("/sentiment/")
async def sentiment_analysis(message: Message):
    message.output  = str(nlp.sentiments(message.input))
    return {"output" : message.output}

@app.post("/summarization/")
async def summarization_analysis(message: Message):
    message.output  = str(nlp.summarization(message.input))
    return {"output" : message.output} 

@app.post("/question-answering/")
async def qarization(message: QA):
    return nlp.qarization(message.question, message.context)