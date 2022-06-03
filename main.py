import json
import random
from datetime import datetime

import pywhatkit

now_m_d = datetime.now().strftime("%d%m")


class SendMessage:
    def __init__(self):
        self.time = datetime.now().strftime("%d%m")

    def check_day(self):
        if self.time == '0803':
            with open("data.json", "r", encoding='utf-8') as f:
                book = json.load(f)
            number_for_women_day = []
            for k, v in book.items():
                if v["sex"] == 'female':
                    number_for_women_day.append(v["phone"])
            return number_for_women_day
        elif self.time == '2302':
            with open("data.json", "r", encoding='utf-8') as f:
                book = json.load(f)
            number_for_man_day = []
            for k, v in book.items():
                if v["sex"] == 'female':
                    number_for_man_day.append(v["phone"])
            return number_for_man_day
        else:
            with open("data.json", "r", encoding='utf-8') as f:
                book = json.load(f)
            number_for_birthday = []
            for k, v in book.items():
                v["birthday"] = v["birthday"].replace('.', '')
                if v["birthday"] == now_m_d:
                    number_for_birthday.append(v["phone"])
            return number_for_birthday

    @staticmethod
    def women_day(number_for_women_day):
        with open("women_day.json", "r", encoding='utf-8') as file:
            book_women_day = json.load(file)
        women_day_text = random.choice(list(book_women_day.values()))
        for i in number_for_women_day:
            base = 14
            pywhatkit.sendwhatmsg(i, women_day_text, base, (random.randrange(base, 60, 5)))

    @staticmethod
    def man_day(number_for_man_day):
        with open("man_day.json", "r", encoding='utf-8') as file:
            book_man_day = json.load(file)
        man_day_text = random.choice(list(book_man_day.values()))
        for i in number_for_man_day:
            base = 10
            pywhatkit.sendwhatmsg(i, man_day_text, base, (random.randrange(base, 60, 5)))

    @staticmethod
    def birthday(number_for_birthday):
        with open("birthday.json", "r", encoding='utf-8') as file:
            book_birthday = json.load(file)
        birthday_text = random.choice(list(book_birthday.values()))
        for i in number_for_birthday:
            base = 23
            pywhatkit.sendwhatmsg(i, birthday_text, base, (random.randrange(base, 60, 5)))
        return number_for_birthday


send_message = SendMessage()
print('Bot is started...')
while True:
    if check_day := send_message.check_day():
        send_message.birthday(check_day)
        print('Ready birthday')
        send_message.man_day(check_day)
        print('Ready man_day')
        send_message.women_day(check_day)
        print('Ready women_day')
    else:
        print('no')

# def women_day():
#      if now_m_d == '0803':
#          with open("data.json", "r", encoding='utf-8') as f:
#             book = json.load(f)
#          number_for_women_day = []
#
#          for k, v in book.items():
#             if v["sex"] == 'female':
#                 number_for_women_day.append(v["phone"])
#          with open("women_day.json", "r", encoding='utf-8') as file:
#             book_women_day = json.load(file)
#          women_day_text = random.choice(list(book_women_day.values()))
#          for i in number_for_women_day:
#             base=14
#          pywhatkit.sendwhatmsg(i, women_day_text, base,(random.randrange(base,60,5)))
#
#
# def man_day():
#      if now_m_d == '2302':
#          with open("data.json", "r", encoding='utf-8') as f:
#             book = json.load(f)
#          number_for_man_day = []
#          for k, v in book.items():
#             if v["sex"] == 'female':
#                 number_for_man_day.append(v["phone"])
#          with open("man_day.json", "r", encoding='utf-8') as file:
#             book_man_day = json.load(file)
#          man_day_text = random.choice(list(book_man_day.values()))
#          for i in number_for_man_day:
#             base=14
#          pywhatkit.sendwhatmsg(i, man_day_text, base,(random.randrange(base,60,5)))
#
# def main():
#     with open("data.json", "r", encoding='utf-8') as f:
#         book = json.load(f)
#     number_for_birthday = []
#     for k,v in book.items():
#         v["birthday"] = v["birthday"].replace('.', '')
#         if v["birthday"] == now_m_d:
#             number_for_birthday.append(v["phone"])
#
#     with open("birthday.json", "r", encoding='utf-8') as file:
#         book_birthday = json.load(file)
#
#     birthday_text = random.choice(list(book_birthday.values()))
#     for i in number_for_birthday:
#         base=14
#         pywhatkit.sendwhatmsg(i, birthday_text, base,(random.randrange(base,60,5)))
#
#
# if __name__ == '__main__':
#     main()
#     women_day()
#     man_day()
