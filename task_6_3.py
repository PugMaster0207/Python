class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'имя - {self.name} ,фамилия - {self.surname}')

    def get_total_income(self):
        print(f'общий доход - {self._income.get("wage") + self._income.get("bonus")}')


me = Position('леша', 'болотовский', 'програмист', 30000, 2500)
me.get_full_name()
me.get_total_income()