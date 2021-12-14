#!/usr/bin/env python
import random
import re

import telebot

bot = telebot.TeleBot("5097013736:AAHOj0LU2GXj8dE2DXDMZlg8vFL8QRdhy0Q", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['deadline'], content_types=['text'])
def send_random(message):
    r_c = re.findall(r'\d+', message.text)
    if len(r_c) == 0:
        bot.send_message(message.chat.id, "Ты совсем тупой? Из чего мне выбирать?")
        return
    if len(r_c) == 1:
        bot.send_message(message.chat.id, "Пидор, 2 цифры надо")
        return
    r_min = int(r_c[0])
    r_max = int(r_c[1])
    bot.send_message(message.chat.id, 'Сейчас стоит делать: {}'.format(random.randint(r_min, r_max)))


bot.infinity_polling()
