import pywhatkit
from flask import Flask, request

def send_message():
    list = ['+###########']
    for i in list:
        pywhatkit.sendwhatmsg(i, "Проверяла работу приложения", 13, 27)
    # pywhatkit.sendwhatmsg_to_group_instantly(phone=mobile, message=message)

def main():
    send_message()

if __name__ == '__main__':
    main()
