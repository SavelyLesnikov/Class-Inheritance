class Vehicle:
    __COLOR_VARIANTS = ['Зелёный', 'Синий', 'Красный']

    def __init__(self, owner):
        self.owner = owner
        self.__model = 'Камаз'
        self.__engine_power = 240
        self.__color = 'Белый'
        self.new_color = None

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Михалыч')
vehicle1.print_info()
print('')
vehicle1.set_color('Терракотовый')
print('')
vehicle1.set_color('Зелёный')
vehicle1.owner = 'Петрович'
vehicle1.print_info()
