class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'
    def __init__(self):
        self.y_distance = Eagle.y_distance
        self.sound = Eagle.sound

    def fly(self, dy):
        self.y_distance += dy

class Horse:
    x_distance = 0
    sound = 'Frr'
    def __init__(self):
        x_distance = Horse.x_distance
        sound = Horse.sound
        super().__init__()

    def run(self, dx):
        self.x_distance += dx

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return f'({self.x_distance}, {self.y_distance})'

    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
