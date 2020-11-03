import time
from datetime import datetime
import requests


# Форматирование вывода сообщения
def pretty_message(message):
    dt = datetime.fromtimestamp(message['time'])
    dt_str = dt.strftime('%H:%M:%S')
    print(message['username'], dt_str, sep=', ')
    print(message['text'])
    print()


# Задание порога фильтрации. 0.0, чтобы выводились все сообщения, содержащиеся на сервере
after = 0.0
while True:
    # Получить все сообщения, хранящиеся на сервере
    data = requests.get('http://127.0.0.1:5000/messages', params={'after': after}).json()

    # Вывод каждого сообщения отдельно
    for message in data['messages']:
        pretty_message(message)
        # Чтобы каждый раз не выводились все сообщения, а только новые, обновляем порог
        after = message['time']

    # Делать запрос на сервер 1 раз/сек
    time.sleep(1)