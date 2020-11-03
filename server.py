import time
import random

from flask import Flask, request, Response
from utils import filter_by_key

app = Flask(__name__)

# Список сообщений, отпрпвленных за текущую сессию
messages = []


# Функция типа send - отправка сообщений от клиента серверу
# Метод POST используется для запроса, при котором адресуемый сервер принимает объект
@app.route("/send", methods=['POST'])
def send():
    # Извлечение из JSON-объекта информации
    name = request.json.get('username')  # Имя пользователя
    text = request.json.get('text')  # Текст сообщения

    # Валидация данных сообщения
    if not name or not isinstance(name,
                                  str) or not text:  # Если имя или сообщение не существуют или не являются строкой
        return Response(status=400)  # Вернуть код ошибки 400

    message = {'username': name, 'time': time.time(), 'text': text}  # Формирование сообщения
    messages.append(message)  # Добавление сообщения в "базу" сообщений

    # Место для сообщений ботику
    if text == '/status':
        count = status()
        text = f"Count of users: {count['count_of_users']}.\nCount of messages: {count['count_of_messages']}"
        message = {
            'username': 'Chat-bot (⌒▽⌒)♡',
            'time': time.time(),
            'text': text
        }
        messages.append(message)
        # С этого момента чат-бот тоже входит в число участников чата, и его сообщения тоже считаются

    return Response(status=200)  # 200 - код "ОК"


# Функция для фильтрации сообщений
@app.route("/messages")
def messages_view():
    # Дроп ошибки 400, если порог времени некорректен
    try:
        after = float(request.args['after'])
    except:
        return Response(status=400)

    # Возвращает объект с отфильтрованными сообщениями под ключом 'messages'
    return {
        'messages': filter_by_key(messages, key='time', threshold=after)
    }


# Функция подсчёта количества пользователей и сообщений на сервере в данной сессии
@app.route("/status")
def status():
    # Количество сообщений
    msg_cnt = len(messages)

    # Количество пользователей
    users = []
    for message in messages:
        if message['username'] not in users:
            users.append(message['username'])
    usr_cnt = len(users)

    # Возвращает объект, содержащий необходиммую инфу
    return {
        'count_of_users': usr_cnt,
        'count_of_messages': msg_cnt
    }


app.run()
