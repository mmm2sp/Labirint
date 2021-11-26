import pygame

class Wall:
    '''
    По координатам центра клетки x и y ставим стену,
    параметр orientation отвечает за расположение стены относительно клеточки:
    w - стена сверху
    a - стена слева
    s - стена снизу
    d - стена справа
    '''
    def __init__(self, screen, x, y, color, orientation):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.orientation = str(orientation)
        
    def draw(self):
        '''
        Стена сверху:
        '''
        if self.orientation == 'w':
            pygame.draw.line(self.screen, self.color, (self.x-10,self.y-10), (self.x+10,self.y-10), width=3)
        '''
        Стена снизу:
        '''
        if self.orientation == 's':
            pygame.draw.line(self.screen, self.color, (self.x-10,self.y+10), (self.x+10,self.y+10), width=3)
        '''
        Стена слева:
        '''
        if self.orientation == 'a':
            pygame.draw.line(self.screen, self.color, (self.x-10,self.y-10), (self.x-10,self.y+10), width=3)
        '''
        Стена справа:
        '''
        if self.orientation == 'd':
            pygame.draw.line(self.screen, self.color, (self.x+10,self.y-10), (self.x+10,self.y+10), width=3)
        
class Door(Wall):
    '''
    Рисует дверь по координатам центра клетки
    '''
    def draw_door(self):
        door = Wall(self.screen, self.x, self.y, door.color, door.orientation)

class Key:
    '''
    Рисует ключ по координатам центра клетки
    '''
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-10, self.y-10, 20, 20))
        pygame.draw.line(self.screen, (210, 210, 0), (self.x, self.y+8), (self.x, self.y-8), width = 2)
        pygame.draw.circle(self.screen, (210, 210, 0), (self.x,self.y+8), 5)
        pygame.draw.rect(self.screen, (210, 210, 0), (self.x, self.y-8,3, 4))

class Minotaur:
    '''
    Рисует минотавра по координатам центра клетки
    '''
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-10, self.y-10, 20, 20))
        pygame.draw.polygon(self.screen, (120, 50, 0), [(self.x,self.y+8),(self.x-6,self.y-7),(self.x+6,self.y-7)])
        pygame.draw.polygon(self.screen, (0, 0, 0), [(self.x-5,self.y-7),(self.x-4,self.y-9),(self.x-4,self.y-7)])
        pygame.draw.polygon(self.screen, (0, 0, 0), [(self.x+5,self.y-7),(self.x+4,self.y-9),(self.x+4,self.y-7)])
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x-2,self.y-2), 1)
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x+2,self.y-2), 1)
        
class Revival:
    '''
    Рисует место возрождения после смерти по координатам центра клетки
    '''
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-10, self.y-10, 20, 20))
        pygame.draw.line(self.screen, (255,0,0), (self.x, self.y-8), (self.x, self.y+8), width = 8)
        pygame.draw.line(self.screen, (255,0,0), (self.x-8, self.y), (self.x+8, self.y), width = 8)

class Explored_square:
    '''
    Рисует исследованную клетку по координатам её центра
    '''
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-10, self.y-10, 20, 20))

class Portal:
    '''
    Рисует портал по координатам центра клетки
    '''
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-10, self.y-10, 20, 20))
        pygame.draw.circle(self.screen, (190, 100, 250), (self.x, self.y), 9)
        
class Player:
    '''
    Рисует игрока по координатам центра клетки
    '''
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(self.screen, (0, 200, 0), (self.x-9, self.y-9, 18, 18), width = 3)
class Another_Player:
    '''
    Рисует противника по координатам центра клетки
    '''
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 200), (self.x-9, self.y-9, 18, 18), width = 3)

class Armory:
    '''
    Рисует арсенал по координатам центра клетки
    '''
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-10, self.y-10, 20, 20))
        pygame.draw.line(self.screen, (120, 50, 0), (self.x-8, self.y+8), (self.x-7, self.y+7) , width = 3)
        pygame.draw.polygon(self.screen, (160, 160, 160), [(self.x-6,self.y+8),(self.x-8,self.y+6),(self.x+8,self.y-8)])

class Boundaries:
    def __init__ (self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 0), (self.width/2, 0), (self.width/2, self.height), width = 10)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width/4, 0), (self.width/4, self.height), width = 5)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width*3/4, 0), (self.width*3/4, self.height), width = 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height/3), (self.width, self.height/3), width = 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height*2/3), (self.width, self.height*2/3), width = 5)
        

