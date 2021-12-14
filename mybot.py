"""
high level support for doing this and that.
"""
import os

import telebot

from prettytable import PrettyTable, from_html_one

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
BOT = telebot.TeleBot(TOKEN, parse_mode=None)


@BOT.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    replying.
    """
    BOT.reply_to(message, "Howdy, how are you doing?")


@BOT.message_handler(commands=['table_text'], content_types=['text'])
def send_table(message):
    """
    making table
    """
    table = PrettyTable()
    list_words = message.text.split()
    if len(list_words) < 3:
        BOT.send_message(message.chat.id, 'Не надо так')
        return
    number_of_fields = int(list_words[1])
    if number_of_fields == 0:
        BOT.send_message(message.chat.id, 'Не надо так')
        return
    row = []
    fields = []
    for i in range(3, len(list_words)):
        if i < 3 + number_of_fields:
            fields.append(str(list_words[i]))
        else:
            if i == 3 + number_of_fields:
                table.field_names = fields
            if len(row) == number_of_fields:
                table.add_row(row)
                elem = str(list_words[i])
                if list_words[i].isdigit():
                    elem = int(list_words[i])
                row = [elem]
            else:
                elem = str(list_words[i])
                if list_words[i].isdigit():
                    elem = int(list_words[i])
                row.append(elem)
    table.add_row(row)
    string_s = table.get_string()
    BOT.send_message(message.chat.id,
                     string_s)


@BOT.message_handler(commands=['table_html'], content_types=['text'])
def send_table(message):
    """
    making table
    """
    table = PrettyTable()
    list_words = message.text.split()
    if len(list_words) < 3:
        BOT.send_message(message.chat.id, 'Не надо так')
        return
    number_of_fields = int(list_words[1])
    if number_of_fields == 0:
        BOT.send_message(message.chat.id, 'Не надо так')
        return
    row = []
    fields = []
    for i in range(3, len(list_words)):
        if i < 3 + number_of_fields:
            fields.append(str(list_words[i]))
        else:
            if i == 3 + number_of_fields:
                table.field_names = fields
            if len(row) == number_of_fields:
                table.add_row(row)
                elem = str(list_words[i])
                if list_words[i].isdigit():
                    elem = int(list_words[i])
                row = [elem]
            else:
                elem = str(list_words[i])
                if list_words[i].isdigit():
                    elem = int(list_words[i])
                row.append(elem)
    table.add_row(row)
    string_s = table.get_html_string()
    BOT.send_message(message.chat.id,
                     string_s)


@BOT.message_handler(commands=['to_text'], content_types=['text'])
def send_table(message):
    """
    making table
    """
    list_words = message.text[8:]
    string_s = from_html_one(list_words).get_string()
    BOT.send_message(message.chat.id,
                     string_s)


BOT.infinity_polling()
