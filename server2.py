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


def answer_to_client_step(лабиринт, conn, игроки):
    '''
    отвечает клиенту, смог ли он походить и что в той клетке, куда он пришел
    :param labirint: матрица лабиринта со всей инфой о нем
    :return: ответ, который отправили серверу
    '''
    data = conn.recv(16)  # возможно стоит передавать дату как параметр функции
    answer = 'NN00'
    if data.decode('utf-8') == 'W' or data.decode('utf-8') == 'A' or data.decode('utf-8') == 'S' or data.decode(
            'utf-8') == 'D':
        answer, лабиринт, игроки = игроки[0].move(data.decode('utf-8'), лабиринт, игроки)
        conn.send(answer.encode('utf-8'))
    return answer, лабиринт, игроки

def say_to_client_about_serv_step(data, conn):
    '''
    отправляет данные клиенту о шаге игрока на сервере
    :param conn: канал связи
    :param data: две буквы (строка)
    '''
    conn.send(data.encode('utf-8'))
