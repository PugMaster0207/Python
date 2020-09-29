from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_calc(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def fabric_calc(self):
        return f'на создание пальто уйдет {round(self.V / 6.5 + 0.5, 2)} у.е. ткани'


class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def fabric_calc(self):
        return f'на создание костюма уйдет {round(2 * self.H + 0.3, 2)} у.е. ткани'


a = Coat(35)
print(a.fabric_calc)
b = Suit(50)
print(b.fabric_calc)
