import requests

# Ввод имени пользователя (однократно)
username = input('Input your username: ')

# Цикл ввода и отправки сообщений
while True:
    text = input("Your message: ") # Ввод текста
    # Формирование объекта сообщения
    message = {
        'username': username,
        'text': text
    }
    # Отправить на адресуемый сервер сообщение
    # Параметры: URL, данные в виде JSON-объекта
    requests.post('http://127.0.0.1:5000/send', json=message)

# получить с сервера объект из функции status
# print(requests.get('http://127.0.0.1:5000/status'))

# Преобразование json: словарь -> json -> http-object -> server