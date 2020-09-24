import time


class TrafficLights:
    colour = 'красный'

    def running(self):
        print(self.colour)
        i = time.time()
        j = time.time()
        while True:
            if self.colour == 'красный' and time.time() - i >= 7:
                self.colour = 'желтый'
                i = time.time()
            if self.colour == 'желтый' and time.time() - i >= 2:
                self.colour = 'зеленый'
                i = time.time()
            if self.colour == 'зеленый' and time.time() - i >= 20:
                self.colour = 'красный'
                i = time.time()
            if time.time() - j >= 2:
                print(self.colour)
                j = time.time()


a = TrafficLights()
a.running()
