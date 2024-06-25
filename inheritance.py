class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Animal:
    alive = True
    fed = False
    food = Plant

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = Plant
        if food.edible is True:
            self.fed = True
            print(f'{self.name} съела {food.name}')
        else:
            self.alive = False
            print(f'{self.name} не стала есть {food.name}')


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True
    pass


a1 = Predator('Пантера')
a2 = Mammal('Панда')
p1 = Flower('Пион')
p2 = Fruit('Манго')

print(a1.name)
print(a2.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
