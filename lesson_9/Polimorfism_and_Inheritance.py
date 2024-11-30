# Наследование

class Flowers:
    def smell_and_bloom(self):
        return "Цветут и приятно пахнут"

class Trees:
    def grow_and_root(self):
        return "Растут и укореняются"

class Plants(Flowers, Trees):
    def produce_fruits(self):
        return "Приносят плоды"

apple = Plants()
print(apple.smell_and_bloom())
print(apple.grow_and_root())
print(apple.produce_fruits())

# Полиморфизм

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Audi", "A7")
plane1 = Plane("Boeing", "777")
for x in (car1, plane1):
  x.move()