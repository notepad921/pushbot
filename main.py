# -*- coding: utf-8 -*-

from datetime import date
import telebot
import random

TOKEN = "1209122889:AAEQocM53fjTteFxXsb8G5NZmbnPrRXKcv8"

persons = {"Ольга": "@olgabondar",
           "Алина": "@alice_in_the_field",
           "Ильяс": "@irtimir",
           "Дмитрий": "@zvrvdmtr",
           "Кирилл": "@butusk0",
           "Антон": "@qqwerty228"}

#chat_id = -494735017  # тестовый
chat_id = -1001132572105 # BTEAM


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


def damn_generator():
    damn_noun = ("антихрист", "безобразник", "визгопряха", "каналья", "коломесъ", "курощупъ", "засранец", "баламошка", "елдыга", "межеумокъ")
    damn_adjective = ("псоватый", "криворукий", "дебиловатый", "пупырчатый", "придурковатый", "яйцекладущий", "рукожопый", "облезлый", "глуподырый")
    local_damn = f"{random.choice(damn_noun)} {random.choice(damn_adjective)}"
    return local_damn


def send_push(local_chat_id, local_person, local_damn):
    text = f"{local_person}, {local_damn}, ты сегодня дежуришь!" \
           f"\nhttps://wiki.1cupis.org/display/DBT/Checklists\n\nНу и @NVVitalii, как обычно, {vitaly_damn}."
    bot.send_message(local_chat_id, text)


def send_text(local_chat_id, local_person, local_damn):
    text = f"{local_person}, {local_damn}, ты сегодня дежуришь!"
    print(text)


bot = telebot.TeleBot(TOKEN)

weekday = check_weekday()
person = choose_person(weekday)
damn = damn_generator()
vitaly_damn = damn_generator()

if person is not None:
    send_push(chat_id, person, damn)
else:
    pass
