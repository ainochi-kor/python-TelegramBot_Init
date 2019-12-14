import requests
import urllib.request
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from uuid import uuid4
import logging
import time

#'Token'에 자신의 텔레그램 HTTPS API를 입력하여 주세요.
updater = Updater(token='Token', use_context=True)
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

