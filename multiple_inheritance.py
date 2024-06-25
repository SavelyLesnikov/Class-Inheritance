class Vehicle:
    def __init__(self, vehicle_type, price):
        self.vehicle_type = 'none'
        super().__init__(price)


class Car:
    def __init__(self, price):
        self.price = 1000000
        self.hp = None

    def horse_powers(self, hp=300):
        self.hp = hp
        return self.hp


class Nissan(Vehicle, Car):
    def __init__(self, vehicle_type=None, price=None):
        super().__init__(vehicle_type, price)
        self.vehicle_type = 'Sedan'
        self.price = 500000

    def horse_powers(self):
        return super().horse_powers(200)

    def print_info(self):
        print(f'Type: {self.vehicle_type}\nPrice: {self.price}\nPower: {self.horse_powers()}')


c = Nissan()
c.print_info()
