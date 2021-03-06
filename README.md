# Labirint

## Описание проекта
Курсовой проект. Компьютерная версия "бумажной" игры лабиринт.

Подробнее см. https://ru.wikipedia.org/wiki/Лабиринт_(игра_на_бумаге)

## Описание ПО

Игра для двух игроков, играющих на разных компьютерах, один из которых выполняет функцию сервера (запускать main_server.py), другой -- клиента (запускать main_client.py).

При запуске сервера в меню отобразится его ΙP-адрес, который надо ввести в меню клиента, после чего нажать кнопку "Создать сервер и лабиринт" (на компьютере сервера) и нажать пробел на устройстве клиента.

После этого буден сгенерирован лабиринт, а на мониторах игроков отобразится игровое поле, разделенное на 4 части. На левой половине будут отображаться результаты ходов игрока, а на правой -- его противника (вне зависимости от того, кто из них клиент, а кто сервер).

Флажок, отображаемый на одной из сторон указывает, чей ход. Верхняя часть экрана, отделеная линией служит для отображения уже исследованных частей карты (см. Описание игры).

После того, как один из игроков выйдет из лабиринта будет отображен экран победы / поражения у победившего и проигравшего игрока сответственно.

## Краткое описание игры

Два игрока оказываются в лабиринте на разных пустых клетках. По очереди совершая ходы, они стремятся найти ключ и выйти из лабиринта.

## Цель игры

Найти ключ и с его помощью выйти из лабиринта.

## Управление

В свой ход вы можете попытаться переместиться в соседнюю клетку с помощью клавиш со стрелками, либо совершить попытку выстрела (направление выбирается клавишами WASD), после чего ход перейдет к противнику.

## Описание игры

Лабиринт представляет собой прямоугольник, размером не более, чем 7*7 клеток, но не менее двух в ширину и высоту.

Между некоторыми клетками расположена стена, не позволяющая пройти из одной клетки в другую. Помимо пустых клеток есть клетки с порталами, которые перебрасывают тебя в другую часть лабиринта (игрок не знает, куда именно, поэтому старые куски карты отображаюся в верхней части экрана). Порталы работают по циклу: если в лабиринте n порталов, то из i-го перебрасывает в i+1-й, а из n-го в перавый. Число порталов не менее двух, но не более семи.

Также в лабиринте есть клетка с ключом, где изначально лежит единственный ключ. После того, как один из игроков его подобрал (побывал на этой клетке), он путешествует с игроком. Еще есть клетка-арсенал, где можно получить ножи (у игрока может быть их не более трех). Вместо хода можно бросить нож в одну из соседних клеток и он уничтожит игрока или минотавра, если они там есть. Если игрок попадает на клетку с живым минотавром или его убивает другой игрок, то умерший игрок попадает в больницу, а все его снаряжение (ключ и ножи) остается на клетке, где он погиб.

Дверь -- это одна из внешних стенок лабиринта, через которую можно выйти. При попытке выйти без ключа, она будет показана как стена другого цвета.

## Распределение ролей

Андрей Щербаков: взаимодействие сервер-клиент, взаимодействие с пользователем

Кирилл Живетьев: графические модули

Матвей Муравьев: генерация лабиринта, его обновление в процессе игры. Менеджер и идейный вдохновитель