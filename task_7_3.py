class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __sub__(self, other):
        return Cell(self.number - other.number if self.number > other.number else 'первая клетка и так меньше')

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, row):
        final_str = ''
        while True:
            row_copy = row
            for i in range(row_copy):
                if self.number > 0:
                    final_str += '*'
                    self.number -= 1
                else:
                    return final_str
            final_str += '\n'

    def __str__(self):
        return f'{self.number}'


a = Cell(34)
b = Cell(81)
print(a - b)
print(b - a)
print(a + b)
print(b / a)
print(a * b)
print(a.make_order(5))

