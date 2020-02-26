import os
import telebot
from random import randrange
from flask import Flask, request
import config

bot = telebot.TeleBot(config.token, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=config.webhook)

app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Hello!')

def createfolder(hash):
    folders = []
    for i in range(5):
        folders.append(randrange(10000, 99999))
        os.makedirs(str(folders[i]))
    x = randrange(0,4)
    txt = open(str(folders[x])+'/hash.txt', 'w')
    txt.write(hash)
    return str(folders[x])

@bot.message_handler(content_types=['text'])
def hashreader(m):
    bot.send_message(m.chat.id, createfolder(m.text))

if __name__ == '__main__':
    app.run()