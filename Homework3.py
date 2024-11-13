# Task 1 Привести к целому типу -1.6, 2.99

number_1 = 1.6
print(int(number_1))
number_2 = 2.99
print(int(number_2))

# Task 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

string = "www.my_site.com#about"
string_1 = string.replace("#", "/")
print(string_1)

# Task 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’

word = "stroka"
print(word + "ing")

# Task 4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

a = "Ivanou Ivan"
last_name, first_name = a.split()
updated_name = " ".join([first_name, last_name])
print(updated_name)

# Task 5 Напишите программу которая удаляет пробел в начале, в конце строки

text = "  I love learning Python   "
text_trimmed = text.strip(" ")
print(text_trimmed)

# Task 6 Создайте словарь, связав его с переменной school, и наполните его
# данными которые бы отражали количество учащихся в десяти разных
# классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).

dict = {
    "1a": 15,
    "1b": 16,
    "2a": 19,
    "2d": 24,
    "2b": 19,
    "3a": 15,
    "3b": 17,
    "3c": 21,
    "4a": 17,
    "4b": 21
}
print(dict)

# Task 7. Создайте список и извлеките из него списка второй элемент

mylist = ["apple", "banana", "cherry"]
print(mylist[2])

# 8. Вывести входит ли строка1 в строку2 (пример: employ и employment )

a = "employment"
b = "employ"
if b in a:
    print("yes")


# 9. Вывести нужные символы

x = "My name is Agent Smith"
print(x[1])
print(x[3:16:3])
