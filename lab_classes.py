class Cell:
    '''Класс клетка, хранящий всю необходимую информацию о клетке лабиринта'''    
    def __init__(self, coords, lab, walls_v, walls_h):
        '''
        Заполняет параметры в соответствии с полученными данными
        Args:
            coords: координаты клетки
            lab: матрица лабиринта
            walls_v: матрица вертикальных стенок
            walls_h: матрица горизонатльных стенок
        '''
        self.coords = coords
        self.walls = [['#', '-', '-'], ['|', '#', '#'], ['|', '#', '#']]
        #walls[x][y] задает нужные стены, где x, y отсчитываются вправо и вниз соответственно из данной клетки
        self.equipment = []
        self.heroes = []
        
        self.typ = lab[coords[0]][coords[1]]
        if self.typ == 'K':
            self.equipment.append('k')
        if self.typ == 'M':
            self.heroes.append('M')
        if self.typ[0] == 'G':
            self.heroes.append(self.typ)
            self.typ = '0'
            
        self.walls[0][-1] = walls_h[coords[0]][coords[1]]
        self.walls[0][1] = walls_h[coords[0]][coords[1] + 1]
        self.walls[-1][0] = walls_v[coords[0]][coords[1]]
        self.walls[1][0] = walls_v[coords[0] + 1][coords[1]]

    def kill(self, labirint, players):
        '''
        Уничтожает всех heroes, снаряжение убитого игрока переходит
        в equipment клетки, минотавр меняет тип клетки на 'm'
        Args:
            labirint: матрица лабиринта
            players: список игроков
        Returns:
            labirint: матрица лабиринта
            players: список игроков
        '''
        for hero in self.heroes:
            if hero == 'M':
                self.typ = 'm'
            if hero[0] == 'G':
                player = players[int(hero[1::])]
                for i in range(player.num_bullets):
                    self.equipment.append('b')
                if player.key == True:
                    self.equipment.append('k')
                 #FixMe каждый должен отвечать за свое ...
                coords = find_in_lab(labirint, 'R')
                print('Player', player.num, 'died. Now he is in a hospital')
                #FixMe тут надо иным способом сообщать о смерти игрока
                player.kill(coords)            
                labirint[coords[0]][coords[1]].heroes.append(hero)
        self.heroes = []
        return labirint, players

    def get_equipment(self, players, num):# player):#FixMe мб можно просто селф
        '''
        Перемещает снаряжение клетки в снаряжение игрока.
        Если у игрока должно получиться больше 3х пудек, лищние остаются в клетке
        Args:
            player: походивший игрок
        Returns:
            players: список игроков
        '''
        player = players[num]
        remaining_bullets = []
        for obj in self.equipment:
            if obj == 'b':
                if player.num_bullets < 3: 
                    player.num_bullets += 1
                else:
                    remaining_bullets.append(obj)
            elif obj == 'k':
                player.key = True
        self.equipment == remaining_bullets
        return players
            


class Player:
    '''Класс игрока, хранящий всю необходимую информацию о нем'''
    num_bullets = 0
    key = False
    
    def __init__(self, num, coords):
        '''
        Заполняет параметры в соответствии с полученными данными
        Args:
            num: номер игрока
            coords: координаты клетки старта этого игрока
        '''
        self.coords = list(coords)
        self.num = num

    def shift(self, dr, labirint):
        '''
        Перемещает игрока в соседнюю клетку:
        информация обновится и в списке игроков и в матрице лабиринта
        Args:
            dr: направление хода
        Returns:
            answer: информация о новой клетке
            labirint: матрица лабиринта
        '''
        answer = ''
        cell = labirint[self.coords[0]][self.coords[1]]
        hero = 'G' + str(self.num)
        if cell.walls[dr[0]][dr[1]] == '*':
            cell.heroes.remove(hero)
            self.coords[0] += dr[0]
            self.coords[1] += dr[1]
            cell = labirint[self.coords[0]][self.coords[1]]
            cell.heroes.append(hero)
            answer = cell.typ
        elif labirint[self.coords[0]][self.coords[1]].walls[dr[0]][dr[1]] == '@' and \
           self.key == True:
            #FixMe: тут должно произойти окончание игры 
            answer = 'YOU ARE WINNER'#Надо другой ответ!!!
        else: answer = 'NN'
        return answer, labirint

    def kill(self, coords):
        '''
        Уничтожает все снаряжение игрока и перемещает его в больницу
        :param coords: координаты больницы
        '''
        self.num_bullets = 0
        self.key = False
        self.coords = list(coords)
        
    def fire(self, dr, labirint, players):
        '''
        Реализует попытку выстрела в соседнюю клетку в заданном направлении
        Подразумевает отсутствие стены между клетками
        Args:
            dr: направление стрельбы
            labirint: матрица с лабиринтом
            players: список игроков
        Returns:
            labirint: матрица лабиринта
            players: список игроков
        '''
        if self.num_bullets > 0:
            self.num_bullets -= 1
            if labirint[self.coords[0]][self.coords[1]].walls[dr[0]][dr[1]] == '*':
                x = self.coords[0] + dr[0]
                y = self.coords[1] + dr[1]
                labirint, players = labirint[x][y].kill(labirint, players)
        return labirint, players


    def autoshift(self, labirint):
        '''
        Убивает игрока, если тот оказался в клетке с минотавром
        Телепортирует при попадании в портал
        Добавляет 3 пульки, если оказался в арсенале
        Args:
            labirint: матрица с лабиринтом
        Returns:
            labirint: матрица лабиринта
        '''
        cell = labirint[self.coords[0]][self.coords[1]]
        if cell.typ == 'E':
            self.num_bullets = 3
            
        elif cell.typ == 'M':
            for i in range(self.num_bullets):
                cell.equipment.append('b')
            if self.key == True:
                cell.equipment.append('k')
            #FixMe каждый должен отвечать за свое ...
            coords = find_in_lab(labirint, 'R')
            self.kill(coords)
            hero = 'G' + str(self.num)
            labirint[coords[0]][coords[1]].heroes.append(hero)
            cell.heroes.remove(hero)
            
        elif cell.typ > '0' and cell.typ <= '9':
            #FixMe
            hero = 'G' + str(self.num)
            cell.heroes.remove(hero)
            next_portal = str(int(cell.typ) + 1)
            x, y = find_in_lab(labirint, next_portal)
            if x == -1:
                x, y = find_in_lab(labirint, '1')
            self.coords[0] = x
            self.coords[1] = y
            cell = labirint[self.coords[0]][self.coords[1]]
            cell.heroes.append(hero)
        return labirint

##### main function in lab updating ####
            
#Вызов в формате players[i].move(direction, labirint, players)
            
    def move(self, direction, labirint, players):
        '''
        Осуществляет ход
        Params:
            direction: направление хода в формате wasd
            labirint: матрица лабиринта
            players: список игроков
        Returns:
            answer: ответ в формате сервера
            labirint: матрица лабиринта
            players: список игроков
        '''
        dr = [0, 0]
        if direction.lower() == 'w': dr = [0, -1]
        if direction.lower() == 's': dr = [0, 1]
        if direction.lower() == 'a': dr = [-1, 0]
        if direction.lower() == 'd': dr = [1, 0]
        
        answer = 'Fire'#FixMe
        if direction.islower():
            labirint, players = self.fire(dr, labirint, players)
        else:
            answer, labirint = self.shift(dr, labirint)
            players = labirint[self.coords[0]][self.coords[1]].get_equipment(players, self.num)
            
        labirint = self.autoshift(labirint)
        players = labirint[self.coords[0]][self.coords[1]].get_equipment(players, self.num)
        return answer, labirint, players


def find_in_lab(labirint, typ):
    '''
    Ищет клетку нужного типа в матрице лабиринта. Возвращает координаты последней, или (-1, -1), если нету
    Args:
        labirint: матрица лабиринта
        typ: параметр typ искомой клетки
    Returns:
        coords: список координат
    '''
    coords = [-1, -1]
    for string in labirint:
            for cell in string:
                if cell.typ == typ:
                    coords = cell.coords
    return coords

if __name__ == "__main__":
    print("This module is not for direct call!")
