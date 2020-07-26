from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

bot = ChatBot("Chatsume")

# First, lets train our bot with some data
trainer = ChatterBotCorpusTrainer(bot)

trainer.train('chatterbot.corpus.english')