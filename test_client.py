'''
Тестовый вариант клиента для тестового сервера
'''

import socket

sock = socket.socket()
sock.connect(('192.168.0.104', 9090))

while True:
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    if str(data.decode('utf-8')) == 'ход соперника':
        continue
    if str(data.decode('utf-8')) == 'ваш ход':
        # чтобы нарисовать круг на компьютере сервера нужно написать W
        x = input('введите W:   ')
        sock.send(str.encode(x))

sock.close()
