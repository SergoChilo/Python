class Enemy:
    name = ""
    lives = 0
    def init(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            print(self.name + ' killed')
        else:
            print(self.name + ' has ' + str(self.lives) + ' lives')
class Monster(Enemy):
    def init(self):
        super().__init__('Monster', 3)
class Alien(Enemy):
    def init(self):
        super().__init__('Alien', 5)
m = Monster()
a = Alien()
while True:
    x = input()
    if x == 'exit':
        break
    elif x == 'laser':
        m.hit()
    elif x == 'gun':
        a.hit()