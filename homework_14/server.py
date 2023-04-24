from socket import socket, AF_INET, SOCK_STREAM
import json
from threading import Thread

host = ''
port = 7777

clients = []


# Функция, которая отправляет сообщение всем клиентам, кроме пославшего
def broadcast_message(sock, msg):
    for client in clients:
        if client != sock:
            client.send(msg)


# Функция, которая обрабатывает сообщения от клиентов
def message_handler(sock, addr):
    while True:
        data = sock.recv(1024).decode('utf-8')
        msg = json.loads(data)

        # Если клиент отправил сообщение, то отправляем его всем остальным клиентам
        if 'message' in msg:
            msg = json.dumps({'id': str(sock), 'message': msg['message']}).encode('utf-8')
            broadcast_message(sock, msg)


s = socket(AF_INET, SOCK_STREAM)
s.bind((host, port))
s.listen()

print(f"Server started on port {port}")

while True:
    sock, addr = s.accept()
    clients.append(sock)

    print(f"New client: {sock}")

    # Запускаем поток, который будет обрабатывать сообщения от клиента
    Thread(target=message_handler, args=(sock, addr)).start()