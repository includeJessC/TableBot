"""
high level support for doing this and that.
"""
import random  # for giving random things
import re  # for parsing messages
import os

import telebot

from prettytable import PrettyTable

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
BOT = telebot.TeleBot(TOKEN, parse_mode=None)


@BOT.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    replying.
    """
    BOT.reply_to(message, "Howdy, how are you doing?")


@BOT.message_handler(commands=['deadline'], content_types=['text'])
def send_random(message):
    """
    random number.
    """
    r_c = re.findall(r'\d+', message.text)
    if len(r_c) == 0:
        BOT.send_message(message.chat.id, "Ты совсем тупой? Из чего мне выбирать?")
        return
    if len(r_c) == 1:
        BOT.send_message(message.chat.id, "Пидор, 2 цифры надо")
        return
    r_min = int(r_c[0])
    r_max = int(r_c[1])
    BOT.send_message(message.chat.id,
                     f'Сейчас стоит делать: {random.randint(r_min, r_max)}')


@BOT.message_handler(commands=['table_text'], content_types=['text'])
def send_table(message):
    """
    making table
    """
    table = PrettyTable()
    list_words = re.findall(r'\d+', message.text)
    if len(list_words) < 2:
        BOT.send_message(message.chat.id, 'Не надо так')
        return
    number_of_fields = list_words[0]
    if len(number_of_fields) == 0:
        BOT.send_message(message.chat.id, 'Не надо так')
        return
    row = []
    for i in range(2, len(list_words)):
        if i < len(list_words) + number_of_fields:
            table.field_names.append(list_words[i])
        else:
            if len(row) == number_of_fields:
                table.add_row(row)
                row = []
            else:
                row.append(list_words[i])
    string_s = table.get_string()
    BOT.send_message(message.chat.id,
                     string_s)


BOT.infinity_polling()
