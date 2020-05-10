# -*- coding: utf-8 -*-

from datetime import date
import telebot
import random

TOKEN = "1209122889:AAEQocM53fjTteFxXsb8G5NZmbnPrRXKcv8"

# key:(name, tg nickname, gender)
persons = {0: ("Ольга", "@olgabondar", "female"),
           1: ("Алина", "@alice_in_the_field", "female"),
           2: ("Ильяс", "@irtimir", "male"),
           3: ("Дмитрий", "@zvrvdmtr", "male"),
           4: ("Кирилл", "@butusk0", "male"),
           5: ("Антон", "@@qqwerty228", "male")
           }


chat_id = -494735017  # тестовый
# chat_id = -1001132572105 # BTEAM


def check_weekday():
    local_weekday = date.today().isoweekday()
    return local_weekday


def choose_person(local_weekday):
    """Person selection schedule"""

    if local_weekday is 1:
        local_person = persons.get(1)
    elif local_weekday is 2:
        local_person = persons.get(4)
    elif local_weekday is 3:
        local_person = persons.get(5)
    elif local_weekday is 4:
        local_person = persons.get(3)
    elif local_weekday is 5:
        local_person = persons.get(2)
    else:
        return None
    return local_person


def damn_generator(gender):
    """Generating damn based on the gender of the person"""

    end = "ая" if gender is "female" else "ый"

    damn_adjective = (f"псоват{end}", f"криворук{end}", f"дебиловат{end}", f"пупырчат{end}", f"придурковат{end}",
                      f"блохаст{end}", f"рукожоп{end}", f"облезл{end}", f"ушаст{end}", f"мордат{end}",
                      f"безсоромн{end}", f"королоб{end}", f"безмозгл{end}", f"плешив{end}")

    damn_noun = (("антихрист", "антихристка"), ("безобразник", "безобразница"), ("баламошка", "баламошка"),
                 ("коломесъ", "коломеска"), ("курощупъ", "курощупка"), ("засранец", "засранка"), ("каналья", "каналья"),
                 ("елдыга", "елдыга"), ("межеумокъ", "межеумка"), ("рукоблуд", "визгопряха"), ("куёлда", "куёлда"),
                 ("пеньтюхъ", "загузастка"), ("хандрыга", "хандрыга"))

    if gender is "female":
        local_damn = f"{random.choice(damn_noun)[1]} {random.choice(damn_adjective)}"
    else:
        local_damn = f"{random.choice(damn_noun)[0]} {random.choice(damn_adjective)}"

    return local_damn


def action_generator():
    action_list = ("двигает таски", "продалбывается", "покупает джинсы", "сидит на синках",
                   "сидит на менеджерском стуле", "ест", "торгует скриптой")

    local_action = f"{random.choice(action_list)}"
    return local_action


def send_push(local_chat_id, local_person, local_damn, local_action):
    """Send message via telegram"""

    text = f"{local_person[1]}, {local_damn}, ты сегодня дежуришь!\nhttps://wiki.1cupis.org/display/DBT/Checklists\n\n" \
           f"Ну и @NVVitalii, как обычно, {local_action}, {vitaly_damn}."
    bot.send_message(local_chat_id, text)


def send_text(local_person, local_damn, local_action):
    """testing only"""

    text = f"{local_person[1]}, {local_damn}, ты сегодня дежуришь!\nhttps://wiki.1cupis.org/display/DBT/Checklists\n\n" \
           f"Ну и @NVVitalii, как обычно, {local_action}, {vitaly_damn}."
    print(text)


bot = telebot.TeleBot(TOKEN)

weekday = check_weekday()
person = choose_person(weekday)
action = action_generator()
damn = damn_generator(person[2])
vitaly_damn = damn_generator("male")


if person is not None:
    send_push(chat_id, person, damn, action)
else:
    pass
