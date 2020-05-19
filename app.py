from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)


bot = ChatBot("Candice")
bot.set_trainer(ListTrainer)
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")


@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return "str(bot.get_response(userText)) "

if __name__ == "__main__":    
    app.run()
