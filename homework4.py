# Работа с переменными:
#  1. Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".
from enum import unique

var_int = 10
var_float = 8.4
var_str = "No"

# 2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза, результат свяжите с переменной big_int.

big_int = var_int * 3.5

# 3. Измените значение, хранимое в переменной var_float, уменьшив его на единицу,результат свяжите с той же переменной.

var_float = var_float - 1

# 4. Разделите var_int на var_float, а затем big_int на var_float.Результат не привязывайте ни к каким переменным.

print(var_int/var_float)
print(big_int/var_float)

# 5. Измените значение переменной var_str на "NoNoYesYesYes". Используйте конкатенацию (+) и повторение строки (*).

var_str = ("No" * 2 + "Yes" * 3)

# 6. Выведите значения всех переменных.

print(var_int)
print(var_float)
print(var_str)
print(big_int)
print(var_float)

# Строки:
#  1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
#  Извлеките из строки первый символ, затем последний, третий с начала и третий с
#  конца. Измерьте длину вашей строки.

str1 = "We process data"
print(str1[0])
print(str1[-1])
print(str1[3])
print(str1[-3])
print(len(str1))

#  2. Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из
#  нее следующие срезы:
#  ● первые восемь символов
#  ● четыре символа из центра строки
#  ● символы с индексами кратными трем
#  ● переверните строку

str2 = "Select one or multiple newsletters"
print(str2[:8])
print(str2[15:20])
print(str2[0:35:3])
print(str2[::-1])
rev_str2 = "".join(reversed(str2)) # Variant 2
print(rev_str2)

#  3. Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.

name = "Kate"
print(f"my name is {name}")

#  4. Есть строка: test_tring = "Hello world!", необходимо
#  ● напечатать на каком месте находится буква w
#  ● кол-во букв l
#  ● Проверить начинается ли строка с подстроки: “Hello”
#  ● Проверить заканчивается ли строка подстрокой: “qwe”

test_tring = "Hello world!"
print(test_tring.find("w"))
print(test_tring.count("l"))
print(test_tring.startswith("Hello"))
print(test_tring.endswith("qwe"))

# Списки

list1 = ["Piotr", "Paulina", "Maryia"]
list2 = ["dog", "cat", "budgie", "tortoise"]
print(list1[1])
list2 = ["dog", "cat", "budgie", "mouse"]
print(list2)
list_combined = list1 + list2
print(list_combined)
list_changed = list_combined[1:6:1]
print(list_changed)
new_elements = ["Mike", "hamster"]
list_changed.extend(new_elements)
print(list_changed)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c_set = set(a) & set(b)
print(list(c_set))
x = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
y = list(set(x))
print(y)

# Логические операции:
#  1. Присвойте двум переменным любые числовые значения.

num1 = 2
num2 = 8

#  2. Составьте четыре сложных логических выражения с помощью оператора and, два из
#  которых должны давать истину, а два других - ложь.

print(num1 < num2 and num1 * 4 == num2)
print(num1 > 0 and num2 > 0)
print(num1 > num2 and num2 > 0)
print(num1 - 1 == num2 and num1**4 > 0)

#  3. Аналогично выполните п. 2, но уже используя оператор or.

print(num1 < num2 or num1 * 4 == num2)
print(num1 > 0 or num2 > 0)
print(num1 > num2 or num2 < 0)
print(num1 - 1 == num2 or num1**4 < num2)

#  4. Попробуйте использовать в сложных логических выражениях работу с переменными строкового типа.
name1 = "Katrin"
name2 = "John"
print(name1 == name2 or type(name1) == type(name2))
print(len(name1) == len(name2) and type(name1) == type(name2))
print(len(name1) > len(name2) and name1.startswith("K") == True)

# Словари

school = {
    "1a": 13,
    "1b": 18,
    "1c": 23,
    "2a": 26,
    "3a": 24,
    "3b": 19,
    "4a": 17,
    "4b": 22,
    "4c": 19,
    "4d": 18
}
print(school["1a"])
print(school["2a"])
school["1a"] = 15
school["1b"] = 17
school["1c"] = 20
school["5a"] = 21
school.update({"5b": 28})
school.pop("4d")
print(school)

# Преобразование типов. Перевести строку в массив

str_1 =  "Robin Singh"
array = str_1.split(" ")
print(array)

# Дан список. Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

new_list =  ["Ivan", "Ivanou"]
str_2 = "Minsk"
str_3 = "Belarus"
print("Привет, " + " ".join(new_list) + "! Добро пожаловать в " + str_2 + " "+ str_3)

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] - сделайте из него строку

list_4 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(list_4))

# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
#  удалите элемент из списка под индексом 6

list_5 = ["Capitan", "Jack","Sparrow", "Elizabeth", "David", "Jones", "Mermaid", "Pirate", "Witch"]
list_5.insert(3, "princess")
list_5.pop(6)
print(list_5)

#  Необходимо объединить 2 словаря по ключам, а значения ключей поместить в список, если у
#  одного словаря есть ключ "а", а у другого нету, то поставить значение None на
#  соответствующую позицию

a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': 5}
c = {k:[a.get(k, None), b.get(k, None)] for k in sorted(set(a)|set(b))}
print(c)

# Вывести уникальное число из массива

array1 =  [1, 5, 2, 9, 2, 9, 1]

def find_unique_element(array1):
    for element in array1:
        if array1.count(element) == 1:
            return element
    return None

print(find_unique_element(array1))

# найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.

text = "I am Kate. I am from Belarus."
text = text.lower()
letters = [char for char in text if char.isalpha()]
unique_letters = set(letters)
most_common_letter = max(unique_letters, key = letters.count)
print(most_common_letter)

#  Условия
# Дано целое число. Если оно является положительным, то прибавить к нему 1; в
#  противном случае не изменять его. Вывести полученное число.

pos_number = int(input("Введите число: "))
if pos_number > 0:
    print(pos_number + 1)
else:
    print(pos_number)

# Даны три целых числа. Найти количество положительных чисел в исходном наборе.

a1 = int(input("Введите первое число: "))
b1 = int(input("Введите второе число: "))
c1 = int(input("Введите третье число: "))
pos_count = 0
if a1 > 0:
   pos_count += 1
if b1 > 0:
   pos_count += 1
if c1 > 0:
   pos_count += 1
print(pos_count)

#  Дан номер года (положительное целое число). Определить количество дней в этом году

year = int(input("введите год: "))
if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
    print("В этом году 366 дней")
else:
    print("В этом году 365 дней")

#  Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
#  соответствующее данному числу

x = int(input("Введите значение от 1 до 7: "))
if x == 1:
    print("1 - Monday")
elif x == 2:
    print("2 - Tuesday")
elif x == 3:
    print("3 - Wednesday")
elif x == 4:
    print("4 - Thursday")
elif x == 5:
    print("5 - Friday")
elif x == 6:
    print("6 - Saturday")
elif x == 7:
    print("7 -Sunday")
else:
    print("Bad request")

# Variant 2

# week = {1: "Пн", 2: "Вт",
#          3: "Ср", 4: "Чт", 5: "Пт",
#         6: "Сб", 7: "Вс"}
# int_week = int(input("Введите от 1 до 7 :  "))
# if int_week <= 0 or int_week > 7:
#     print("Введено неверное значение")
# else:
#     print(week.get(int_week))

# Найти массу тела в килограммах.

unit = {1: "Килограмм", 2: "Миллиграмм", 3: "грамм", 4: "Тонна", 5: "Центнер"}
int_unit = int(input("Введите значение от 1 до 5: "))
if int_unit == 1:
    print("1 кг")
elif int_unit == 2:
    print("0.000002 кг")
elif int_unit == 3:
    print("0.003 кг")
elif int_unit == 4:
    print("4000 кг")
elif int_unit == 5:
    print("500000 кг")
else:
    print("Wrong number")

#  # Цикл for
#  # 1. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B включительно.

A = int(input("Введите А: "))
B = int(input("Введите B: "))
sum = 0
for i in range(A, B + 1):
    sum += 1
print(sum)

#  # 2. Найти сумму всех натуральных чисел в от A до B

A1 = int(input("Введите А1: "))
B1 = int(input("Введите B1: "))
sum1 = 0
for i in range(A1, B1):
    sum1 += i
print(sum1)

#  # 3. Найти произведение положительных, сумму и количество отрицательных
#  # из 10 введенных целых значений.

product_positive = 1
sum_negative = 0
count_negative = 0
for i in range(10):
    num = int(input(f"Введите целое число ({i + 1}/10): "))
    if num > 0:
        product_positive *= num
    elif num < 0:
        sum_negative += num
        count_negative += 1
print("Произведение положительных чисел:", product_positive)
print("Сумма отрицательных чисел:", sum_negative)
print("Количество отрицательных чисел:", count_negative)

# Дан словарь пловцов с их результатами. Напечатать лучший результат
#  заплыва среди 6 участников.

participants = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17
}

best_result = min(participants.values())
print(best_result)

# min_value = float("Inf")
# for value in participants.values():
#     if value < min_value:
#         min_value = value
# print(min_value)

# Напишите программу, которая будет выводить уникальное число

ar = [1, 5, 2, 9, 2, 9, 1]
unique_number = 0
for num in ar:
    unique_number ^= num
print(unique_number)

# # Цикл while
# # Дано число N. Найти произведение всех чисел от 0 до N.

N = int(input("Enter the number: "))
mltpl = 1
i = 1
while i < N:
     mltpl *= i
     i += 1
print(mltpl)

# Через сколько лет площадь первых сортов будет
#  составлять меньше 10% от площади вторых сортов.

S1 = int(input("Enter S1: "))
S2 = int(input("Enter S2: "))
i = 0
while S1  >= S2 * 0.1:
    S1 = 2 * S1
    S2 = 3 * S2
    i += 1

print(i)

# Дано целое число R (>0). Используя операции деления нацело и взятия
#  остатка от деления, найти количество и сумму его цифр.

R = int(input("Enter R: "))
ostatok = 0
tseloe = 0
while R > 0 :
    tseloe = R // 10
    ostatok = R % 10
    break

print(tseloe)
print(ostatok)
print(ostatok + tseloe)

# Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
#  внука.  И сколько при этом лет будет деду и внуку.

M = int(input("Enter M: "))
N = int(input("Enter N: "))
i = 0
while (N + i)* 2 != M + i:
    i += 1
print(i)
print(N + i)
print(M + i)