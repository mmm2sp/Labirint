from lab_generation import generate

def test_function():
    лабиринт, игроки = generate()
    направление = 'W'

    while направление != '0':
        for i in range(2):
            print('Ходит игрок', i)
            направление = input()
            ответ, лабиринт, игроки = игроки[i].move(направление, лабиринт, игроки)
            print(ответ)

if __name__ == "__main__":
    print("This module was created for DEVELOPERS ONLY!")
    test_function()
   
