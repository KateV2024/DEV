# Наследование

class Plants:
    def grow_and_root(self):
        return "Имеют листья и корни"

class Trees (Plants):
    def type_of_plants(self):
        return "Один из видов растений"

class Flowers (Plants):
    def bloom_and_smell(self):
        return "Цветут"

apple = Trees()
rose = Flowers()

print(apple.grow_and_root())
print(apple.type_of_plants())
print(rose.grow_and_root())
print(rose.bloom_and_smell())

# Полиморфизм

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Drive!")
#
# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Fly!")
#
# car1 = Car("Audi", "A7")
# plane1 = Plane("Boeing", "777")
# for x in (car1, plane1):
#   x.move()