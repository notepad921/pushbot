# -*- coding: utf-8 -*-

import random
import requests
from requests import adapters
from datetime import date

import telebot

import settings


def check_is_day_off():
    """Get data about working/non working day from isdayoff.ru
    0 - working day
    1 - day-off
    100 - wrong date
    101 - not found"""

    local_date = date.today().isoformat().replace("-", "")

    requests.adapters.DEFAULT_RETRIES = settings.DEFAULT_RETRIES
    url = f"http://isdayoff.ru/{local_date}"

    try:
        local_is_day_off = requests.get(url).text
    except requests.exceptions.ConnectionError:
        print("No connection with isdayoff.ru")
        local_is_day_off = None

    return False if local_is_day_off is "0" else True


def check_weekday():
    local_weekday = date.today().isoweekday()
    return local_weekday


def choose_person(local_weekday):
    """Person selection schedule"""

    if local_weekday is 1:
        local_person = settings.persons.get(0)
    elif local_weekday is 2:
        local_person = settings.persons.get(1)
    elif local_weekday is 3:
        local_person = settings.persons.get(2)
    elif local_weekday is 4:
        local_person = settings.persons.get(3)
    elif local_weekday is 5:
        local_person = settings.persons.get(4)
    else:
        return None
    return local_person


def check_gender(local_person):
    return local_person[2]


def damn_generator(local_gender):
    """Generating damn based on the gender of the person"""

    end = "ая" if local_gender is "female" else "ый"

    if gender is "female":
        noun = damn_noun_list.pop(random.randint(0, len(damn_noun_list)-1))[1]
        adjective = damn_adjective_list.pop(random.randint(0, len(damn_adjective_list)-1)) + end
    else:
        noun = damn_noun_list.pop(random.randint(0, len(damn_noun_list) - 1))[0]
        adjective = damn_adjective_list.pop(random.randint(0, len(damn_adjective_list) - 1)) + end

    local_damn = f"{noun} {adjective}"

    return local_damn


def action_generator():
    action_list = ("двигает таски", "продалбывается", "покупает джинсы", "сидит на синках",
                   "сидит на менеджерском стуле", "ест", "не борется с Дмитрием", "торгует скриптой")

    local_action = f"{random.choice(action_list)}"
    return local_action


def send_push(local_chat_id, local_person, local_damn, local_action, local_manager):
    """Send message via telegram"""

    text = f"{local_person[1]}, {local_damn}, ты сегодня дежуришь!\nhttps://wiki.1cupis.org/display/DBT/Checklists\n\n" \
           f"Ну и {local_manager[1]}, как обычно, {local_action}, {manager_damn}."
    bot.send_message(local_chat_id, text)


def send_text(local_person, local_damn, local_action, local_manager):
    """testing only"""

    text = f"{local_person[1]}, {local_damn}, ты сегодня дежуришь!\nhttps://wiki.1cupis.org/display/DBT/Checklists\n\n" \
           f"Ну и {local_manager[1]}, как обычно, {local_action}, {manager_damn}."
    print(text)


bot = telebot.TeleBot(settings.TOKEN)

damn_noun_list = settings.damn_noun_list.copy()
damn_adjective_list = settings.damn_adjective_list.copy()

manager = settings.persons.get("manager")
weekday = check_weekday()
is_day_off = check_is_day_off()
person = choose_person(weekday)
gender = check_gender(person)
action = action_generator()

damn = damn_generator(gender) if person else None
manager_damn = damn_generator(manager[2])


if person and (is_day_off is False):
    send_text(person, damn, action, manager)
else:
    print("Сегодня не дежурим")
