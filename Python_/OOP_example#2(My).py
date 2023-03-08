class count():
    number = int(input('Enter your number : '))
    x = 10

    def init(self, number, x):
        self.number = number
        self.x = x

    def calc_number(self):
        if self.number % self.x == 0:
            print(f'{self.number} divided by {self.x}')
        self.x -= 1
        while self.x != 0:
            return self.calc_number()
        else:
            exit()


class hand(count):
    def process(self, number):
        super().__init__(number)
        super().calc_number()


h = hand()
h.calc_number()
