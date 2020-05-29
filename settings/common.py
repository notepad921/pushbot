
TOKEN = ""  # Telegram bot token

DEFAULT_RETRIES = 5  # number of attempts to get data from http://isdayoff.ru


# key:(name, tg nickname, gender "male" or "female")
person_list = {0: ("Name", "@nickname", "male / female"),  # monday
               1: (),  # tuesday
               2: (),  # wednesday
               3: (),  # thursday
               4: (),  # friday
           "manager": ("Name", "@nickname", "male / female")
               }

link = "https://www.google.com/"  # link to duty info for message

chat_id = int
