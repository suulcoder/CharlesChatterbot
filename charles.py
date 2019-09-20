"""
Charles is an algorithm that uses the ChatterBot librery 
to make an alternative tool to develop the ChatBot of 
Chopin.mol Charles measn Chopin artifitial robot leading
in every selling. This script was developed by Saul
Contreras (SuulCoder).

The following pages were taken as reference:

        https://chatterbot.readthedocs.io
        https://pypi.org/project/ChatterBot/
"""

#Import all important libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import UbuntuCorpusTrainer


#Instantiate a new chatbot named Charles stored in sqlite
bot = ChatBot(
    'Charles',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],

    database_uri='sqlite:///database.db'
)

# Trainer for the chatbot with spanish public libraries
trainer = ChatterBotCorpusTrainer(bot)                                  #Train with ChatterBotCorpus
trainer.train("chatterbot.corpus.spanish")
trainer.train("chatterbot.corpus.spanish.greetings")
trainer.train("chatterbot.corpus.spanish.conversations")
#Train with our own data
trainer3 = ListTrainer(bot)
train_list = [line.rstrip(',.') for line in open('1.txt')]
trainer3.train(train_list)
print('Chat with Charles')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()
        bot_response = bot.get_response(user_input)
        print(bot_response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
