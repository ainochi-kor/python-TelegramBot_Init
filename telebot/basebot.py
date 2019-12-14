import requests
import urllib.request
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from uuid import uuid4
import logging
import time

updater = Updater(token='1067399790:AAGYnjc22lE5Q5-7rUCMtizTPGari2z8-zA', use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    text = update.message.text
    chat_id = update.message.chat_id

    if'모해' in text:
        context.bot.send_message(chat_id=chat_id, text='얍')
    else:
        context.bot.send_message(chat_id=chat_id, text='얍얍')

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)

