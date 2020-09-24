class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def concrete_mass_calc(self):
        try:
            mass = int(input('введите массу асфальта в кг - '))
            depth = int(input('введите толщину полотна в см - '))
            print(f'вам поотребуется {mass * depth * self._length * self._width} тонн асфальта')
        except (ValueError, TypeError):
            print('Error!')


while True:
    try:
        Moscow_spb = Road(int(input('введите длинну дороги в метрах - ')),
                          int(input('введите ширину дороги в метрах - ')))
        break
    except ValueError:
        print('Error!')

Moscow_spb.concrete_mass_calc()
