'''
Модуль клиента
Описаны функции для клиента, реализующие взаимодействие между клиентом и сервером
'''

import socket


def connection(IP, Port):
    '''
    Подключается к серверу
    :param IP: адрес сервера, к которому подключаемся
    :param Port: порт, к которому подключаемся
    :return: подключенный сокет
    '''
    sock = socket.socket()
    sock.connect((IP, Port))
    return sock


def ask_server(vector, sock):
    '''
    отправляет запрос на сервер, можно ли сходить в направлении vector
    :param vector: направление, куда хочется сходить wasd
    :return: ответ сервера в виде wasd + буква предмета в клетке, куда пришли
    '''
    sock.send(vector.encode('utf-8'))
    data = sock.recv(1024)
    return data.decode('utf-8')


def catch_server_steps(sock):
    '''
    Ловит инфу от сервера о его ходах
    :param sock: подключенный к серверу сокет
    :return: информацию переданную сервером
    '''
    data = sock.recv(1024)

    return data.decode('utf-8')


