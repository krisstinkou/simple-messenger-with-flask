# simple-messenger-with-flask
Simple messenger with single chat in certain IP-adress on Python

This messenger is written on Python with framework Flask and PyQT5.
In this messenger is available only one chat. User inputs username and text of message and clicks button ">" (send). 
On client is one listbox, where are displayed all messages since server start.

Chat is available for all clients, who send messages on certain IP-adress (mashine, where server work)


Installing Flask:
pip install flask


For starting messaging you need:

<b>1. Run server.py</b>

This fine contains source code of messenger. There described list with message, functions for sending and view messages. 

<b>2. Run messenger.py</b>

Contains Source code for client. This is application for user.


For changing IP-adress: 

In file messenger.py on line window = MyWindow('http://127.0.0.1:5000') change argument of constructor in brackets.


File clientui.py contains code of UI with using PyQT5.

File utils.py contains additional fonctions for messenger.

File messenger.ui - UI of client from Qt Designer.

Directory Test Files - other files.

For changing 
