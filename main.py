#!/usr/bin/python
# -*- coding: utf-8 -*-

import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Петрович в деле")


# sendMessage
bot.send_message(config.chat_id, config.text)
