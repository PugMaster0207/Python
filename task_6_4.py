class Car:
    is_police = None

    def __init__(self, speed, colour, name):
        self.speed = speed
        self.colour = colour
        self.name = name

    def go(self):
        print(f'машина {self.name} поехала')

    def stop(self):
        print(f'машина {self.name} остановилась')

    def turn(self, ):
        direction = input('куда повернет ваша машина? ')
        print(f'машина {self.name} повернула на {direction}')

    def show_speed(self):
        print(f'машина {self.name} едет со скоростью {self.speed}')


class TownCar(Car):
    is_police = False

    def __init__(self, speed, colour, name,):
        super().__init__(speed, colour, name,)

    def show_speed(self):
        print(f'машина {self.name} едет со скоростью {self.speed}', end='')
        if self.speed > 60:
            print(f', и это превышение на {self.speed - 60}км/ч')


class SportCar(Car):
    is_police = False

    def __init__(self, speed, colour, name,):
        super().__init__(speed, colour, name,)


class WorkCar(Car):
    def __init__(self, speed, colour, name, is_police):
        super().__init__(speed, colour, name)
        if is_police == 'да':
            self.is_police = True
        else:
            self.is_police = False

    def show_speed(self):
        print(f'машина {self.name} едет со скоростью {self.speed}', end='')
        if self.speed > 40:
            print(f', и это превышение на {self.speed - 40}км/ч')


class PoliceCar(Car):
    is_police = True

    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name)


a = TownCar(80, 'red', 'olga')
print(a.is_police)
a.go()
# a.turn()
a.show_speed()
a.stop()

b = PoliceCar(120, 'black', 'poly')
print(b.is_police)
b.go()
# b.turn()
b.show_speed()
b.stop()

q = Car(80, 'red', 'olga')
print(q.is_police)

c_1 = WorkCar(3000, 'yellow', 'samsa', 'да')
print(c_1.is_police)

c_2 = WorkCar(3000, 'yellow', 'samsa', 'нет')
print(c_2.is_police)

d = SportCar('wow i cant count to that!', 'speeeeed', 'Lightning mcqueen')
print(d.speed)
print(d.colour)