"""
high level support for doing this and that.
"""
import random  # for giving random things
import re  # for parsing messages

import telebot

BOT = telebot.TeleBot("5097013736:AAHOj0LU2GXj8dE2DXDMZlg8vFL8QRdhy0Q", parse_mode=None)


@BOT.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    replyingk.
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


BOT.infinity_polling()
