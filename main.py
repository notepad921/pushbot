# -*- coding: utf-8 -*-

from datetime import date
import telebot


TOKEN = "1209122889:AAEQocM53fjTteFxXsb8G5NZmbnPrRXKcv8"

persons = {"Ольга": "@olgabondar",
             "Алина": "@alice_in_the_field",
             "Ильяс": "@irtimir",
             "Дмитрий": "@zvrvdmtr",
             "Кирилл": "@butusk0",
             "Антон": "@qqwerty228"}

chat_id = -494735017


def check_weekday():
    local_weekday = date.today().isoweekday()
    return local_weekday


def choose_person(local_weekday):
    if local_weekday is 1:
        local_person = persons.get("Алина")
    elif local_weekday is 2:
        local_person = persons.get("Кирилл")
    elif local_weekday is 3:
        local_person = persons.get("Антон")
    elif local_weekday is 4:
        local_person = persons.get("Дмитрий")
    elif local_weekday is 5:
        local_person = persons.get("Ильяс")
    else:
        return None
    return local_person


def send_push(local_chat_id, local_person):
    text = f"{local_person}, ты сегодня дежуришь"
    bot.send_message(local_chat_id, text)


def send_text(local_chat_id, local_person):
    text = f"{local_person}, ты сегодня дежуришь!"
    print(text)


bot = telebot.TeleBot(TOKEN)

weekday = check_weekday()
person = choose_person(weekday)
send_text(chat_id, person)
