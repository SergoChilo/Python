# Вы создаёте игру - шутер! В игре есть два вида врагов, инопланетяне и монстры.Вы
# стреляете по инопланетянам с помощью laser, а по монстрам с помощью gun.
# Каждое попадание уменьшает жизни врагов на 1. Данный код объявляет базовый
# класс Enemy, а также классы Alien и Monster с соответствующим количеством
# жизней.Он также определяет метод hit() для класса Enemy.Вам нужно сделать
# следующее, чтобы завершить программу: 1. Унаследовать классы Alien и Monster
# из класса Enemy. 2. Завершить цикл while , который беспрерывно принимает выбранное
# оружие из пользовательского ввода и вызывает метод hit() соответствующего объекта.
# Пример входных данных : laser
#                         laser
#                         gun
#                         exit
# Пример выходных данных: Alien has 4 lives
#                         Alien has 3 lives
#                         Monster has 2 lives
class Enemy:
    name = ""
    lives = int(input('Enter your lives : '))  # Kolichestvo jizni

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives -= 1
        if self.lives > 0:
            print(self.name + ' killed !!!', ' has ' + str(self.lives) + ' lives')
        elif self.lives == 0:
            print(self.name + ' has ' + str(self.lives) + ' lives')
            exit()


class Monster(Enemy):
    def init(self, name, lives):
        super().__init__(self)


class Alien(Enemy):
    def init(self, name, lives):
        super().__init__(self)


m = Monster('Monster', 3)
a = Alien('Alien', 5)

while True:
    x = input('Enter your weapon : laser / gun     ')
    if x == 'exit':
        break
    elif x == 'gun':
        m.hit()
    elif x == 'laser':
        a.hit()
    else:
        print('Please enter only laser or gun !!!!!')
