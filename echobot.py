#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import time
import threading
import random
import signal
from datamodel import Datamodel
from paragraphs import PARAGRAPHS

DS_FILE = 'reader_bot.json'
MSG_INTERVAL_SECONDS = 3600 * 4
API_TOKEN = '1409783452:AAEwuxQrdHqtd9vHGVs7b1BBAf9rCIkiYhs'
bot = telebot.TeleBot(API_TOKEN)
data = Datamodel(DS_FILE)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\n\
Send /subscribe to subscribe to receive throughout the day some paragraph from a book.\n\
Send /unsubscribe to stop receiving paragraphs.
""")

@bot.message_handler(commands=['subscribe'])
def subscribe(message):
    data.add_user(message.chat.id)
@bot.message_handler(commands=['unsubscribe'])
def subscribe(message):
    data.remove_user(message.chat.id)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
def send_paragraph():
    users = data.get_users()
    random_paragraph_id = random.randint(0, len(PARAGRAPHS))
    paragraph = PARAGRAPHS[random_paragraph_id]
    for user in users:
        bot.send_message(user, paragraph)
def timer_spawner():
    while True:
        timer = threading.Timer(MSG_INTERVAL_SECONDS, send_paragraph).start()
        time.sleep(MSG_INTERVAL_SECONDS)
print('Working')
threading.Thread(target=timer_spawner).start()

bot.polling()


