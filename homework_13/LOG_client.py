from socket import socket, AF_INET, SOCK_STREAM
import json
from threading import Thread

host = 'localhost'
port = 7777


# Функция, которая отправляет сообщение на сервер
def send_msg():
    while True:
        message = input()

        msg = {'message': message}

        s.send(json.dumps(msg).encode('utf-8'))


# Функция, которая получает сообщения от сервера
def receive_msg():
    while True:
        data = s.recv(1024).decode('utf-8')
        msg = json.loads(data)

        # Если сообщение пришло от другого клиента, то выводим его на экран
        if msg['id'] != client_id:
            print(f"Client {msg['id']}: {msg['message']}")


# Создаем сокет и подключаемся к серверу
s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))

# Генерируем id клиента и отправляем его на сервер
client_id = str(hash(s))
msg = {'id': client_id}
s.send(json.dumps(msg).encode('utf-8'))

# Запускаем потоки отправки и получения сообщений
Thread(target=send_msg).start()
Thread(target=receive_msg).start()