# Создать лямбда функцию, которая принимает на вход список имен
# и выводит его в формате "Hello, {name}" вдругой список

func = lambda name: f"Hello, {name}"

def find_name(names):
    greetings = [ ]
    for name in names:
        greetings.append(func(name))
    return greetings

names = {"Sveta", "Sasha", "Kate"}
new_list = find_name(names)
print(new_list)