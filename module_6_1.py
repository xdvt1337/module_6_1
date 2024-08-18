# Родительские классы:
class Animal:
    def __init__(self, name):
        self.alive = True # Живой
        self.fed = False # накормленный
        self.name = name # индивидуальное название каждого животного

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = False
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = True


class Plant:
    def __init__(self, name):
        self.edible = True # съедобность
        self.name = name # индивидуальное название каждого растения



# Дочерние классы:

# Animal:
class Mammal(Animal):
    pass

class Predator(Animal):
    pass

# Plant:
class Flower(Plant):
    pass

class Fruit(Plant):
    pass

# Проверка:
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
