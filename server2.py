'''
Модуль сервера
Описаны функции для сервера, реализующие взаимодействие между клиентом и сервером
'''

import socket


def connection(IP, Port):
    '''
    Открывает порт для соединения с клиентом
    :param IP: адрес сервера
    :param Port: порт для подключения
    :return: печатает, что соединение произошло, возвращает канал связи
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP, Port))
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected:', addr)

    return conn


def answer_to_client_step(labirint, conn):
    '''
    отвечает клиенту, смог ли он походить и что в той клетке, куда он пришел
    :param labirint: матрица лабиринта со всей инфой о нем
    :return: ответ, который отправили серверу
    '''
    data = conn.recv(1024)  # возможно стоит передавать дату как параметр функции
    if data.decode('utf-8') == 'W' or data.decode('utf-8') == 'A' or data.decode('utf-8') == 'S' or data.decode('utf-8') == 'D':
        answer = check(data.decode('utf-8'), labirint)  # - функция проверяющая можно ли туда ходить (параметры WASD), находится в модуле лабиринт
        conn.send(answer.encode('utf-8'))
        return answer

def say_to_client_about_serv_step(data, conn):
    '''
    отправляет данные клиенту о шаге игрока на сервере
    :param conn: канал связи
    :param data: две буквы (строка)
    '''
    conn.send(data.encode('utf-8'))

def check(data, labirint):
    '''
    проверяет можно ли сходить
    :param data: строка с направлением хода wasd
    :param labirint: нформация о лабиринте
    :return:
    '''
    # для проверки лабиринт пуст, сходить можно везде, везде пустые клетки
    info = data + 'N'
    return info