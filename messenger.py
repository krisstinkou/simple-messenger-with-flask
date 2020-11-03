from datetime import datetime
import requests
from PyQt5 import QtWidgets, QtCore
import clientui


class MyWindow(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self, server_url):
        super().__init__()
        self.setupUi(self)
        self.send.pressed.connect(self.send_message)
        self.after = 0
        self.server_url = server_url
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.load_messages)
        self.timer.start(1000)

    def pretty_message(self, message):
        dt = datetime.fromtimestamp(message['time'])
        dt_str = dt.strftime('%H:%M:%S')
        self.messages.append(message['username'] + ', ' + dt_str)
        self.messages.append(message['text'])
        self.messages.append('')
        self.messages.repaint()

    def load_messages(self):
        try:
            data = requests.get(self.server_url + '/messages', params={'after': self.after}).json()
        except:
            return

        for message in data['messages']:
            self.pretty_message(message)
            self.after = message['time']

    def send_message(self):
        username = self.username.text()
        text = self.text.toPlainText()

        message = {
            'username': username,
            'text': text
        }

        try:
            response = requests.post(self.server_url + '/send', json=message)
        except:
            self.messages.append('Сервер недоступен. Повторите попытку позже.')
            self.messages.repaint()
            return
        if response.status_code != 200:
            self.messages.append('Введены некорректные данные.')
            self.messages.repaint()
            return

        self.text.setText('')
        self.text.repaint()


app = QtWidgets.QApplication([])
window = MyWindow('http://127.0.0.1:5000')
window.show()
app.exec_()
