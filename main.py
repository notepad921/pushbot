# -*- coding: utf-8 -*-

import random
import requests
from requests import adapters
from datetime import date

import telebot

import settings


def check_is_day_off(local_date):
    """Get data about working/non working day from isdayoff.ru
    0 - working day
    1 - day-off
    100 - wrong date
    101 - not found"""

    formatted_date = local_date.isoformat().replace("-", "")  # formatting date to view "YYYYMMDD" for correct request
    requests.adapters.DEFAULT_RETRIES = settings.DEFAULT_RETRIES
    url = f"http://isdayoff.ru/{formatted_date}"

    try:
        local_is_day_off = requests.get(url).text
    except requests.exceptions.ConnectionError:
        print("No connection with isdayoff.ru")
        local_is_day_off = None

    return False if local_is_day_off is "0" else True


def check_weekday(local_date):
    local_weekday = local_date.isoweekday()
    return local_weekday


def choose_person(local_weekday, local_person_list):
    """Person selection schedule"""

    if local_weekday is 1:
        local_person = local_person_list.get(0)
    elif local_weekday is 2:
        local_person = local_person_list.get(1)
    elif local_weekday is 3:
        local_person = local_person_list.get(2)
    elif local_weekday is 4:
        local_person = local_person_list.get(3)
    elif local_weekday is 5:
        local_person = local_person_list.get(4)
    else:
        return None
    return local_person


def check_gender(local_person):
    """Gender checking is based on "persons" from local.py"""
    return local_person[2]


def damn_generator(local_gender, local_damn_noun_list, local_damn_adjective_list):
    """Damn generating is based on the person`s gender"""

    end = "ая" if local_gender is "female" else "ый"
    noun_list_len = len(local_damn_noun_list)
    adj_list_len = len(local_damn_adjective_list)

    if gender is "female":
        noun = local_damn_noun_list.pop(random.randint(0, noun_list_len-1))[1]
        adjective = local_damn_adjective_list.pop(random.randint(0, adj_list_len-1)) + end
    else:
        noun = local_damn_noun_list.pop(random.randint(0, noun_list_len-1))[0]
        adjective = local_damn_adjective_list.pop(random.randint(0, adj_list_len-1)) + end

    local_damn = f"{noun} {adjective}"

    return local_damn


def action_generator(local_manager_action_list):
    """Generating manager`s action"""

    local_action = f"{random.choice(local_manager_action_list)}"
    return local_action


def send_push(local_chat_id, local_person, local_damn, local_action, local_manager, local_link):
    """Send message via telegram"""

    text = f"{local_person[1]}, {local_damn}, ты сегодня дежуришь!\n{local_link}\n\n" \
           f"Ну и {local_manager[1]}, как обычно, {local_action}, {manager_damn}."
    bot.send_message(local_chat_id, text)


def send_text(local_person, local_damn, local_action, local_manager, local_link):
    """testing only"""

    text = f"{local_person[1]}, {local_damn}, ты сегодня дежуришь!\n{local_link}\n\n" \
           f"Ну и {local_manager[1]}, как обычно, {local_action}, {manager_damn}."
    print(text)


bot = telebot.TeleBot(settings.TOKEN)

damn_noun_list = settings.damn_noun_list.copy()
damn_adjective_list = settings.damn_adjective_list.copy()

weekday = check_weekday(date.today())
is_day_off = check_is_day_off(date.today())

manager = settings.person_list.get("manager")
person = choose_person(weekday, settings.person_list)
gender = check_gender(person)

action = action_generator(settings.manager_action_list)
damn = damn_generator(gender, damn_noun_list, damn_adjective_list) if person else None
manager_damn = damn_generator(manager[2], damn_noun_list, damn_adjective_list)


if person and (is_day_off is False):
    send_text(person, damn, action, manager, settings.link)
else:
    print("Сегодня не дежурим")
