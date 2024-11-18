# Напищите программу, которая заменит символ “#” на символ “/” в строке 'www.my_site.com#about'

def replace_element(word1):
    word1 = word1.replace("#", "/")
    return word1

word1 = "www.my_site.com#about"
new_word = replace_element(word1)
print(new_word)

# Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’

def add_element(word):
    word = word + "ing"
    return word

word = "stroka"
result = add_element(word)
print(result)

# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

def change_place(surname_name):
    last_name, first_name = surname_name.split()
    updated_name = " ".join([first_name, last_name])
    return updated_name

surname_name = "Иванов Иван"
new_name = change_place(surname_name)
print(new_name)

# Вывести входит ли строка1 в строку2 (пример: employ и employment )

def str1_included_in_str2(str1, str2):
    if str1 in str2:
        return str1 in str2
    else:
        return False

str1 = "employ"
str2 = "employment"
result1 = str1_included_in_str2(str1, str2)
print(result1)

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] - сделайте из него строку

def make_str(c):
    c = " ".join(c)
    return c

c = ["I", "love", "arrays", "they", "are", "my", "favorite"]
new_c = make_str(c)
print(new_c)

# Дано целое число в диапазоне 1–7. Вывести строку — название дня недели, соответствующее данному числу

# def find_weekday(dict, key):
#     if key in dict:
#         return dict[key]
#     else:
#         return "error"
# dict = {1: "Mon", 2: "Tue",3: "Wed", 4: "Thur", 5: "Fri", 6: "Sat", 7: "Sun"}
# key = int(input("Enter the number: "))
# v = find_weekday(dict, key)
# print(f"Day is {v}")

# # Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
# #  внука.  И сколько при этом лет будет деду и внуку.

def find_year( M, N, i):

    while (N + i)* 2 != M + i:
        i += 1
    return M + i, N + i, i

M = int(input("Enter M: "))
N = int(input("Enter N: "))
i = 0
let = find_year(M , N , i)
grandfather_age, grandson_age, years = let
print(f"Деду будет {grandfather_age}, внуку {grandson_age}  через {years} лет")
