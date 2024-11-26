# лексикографическое возрастание

number_names = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen"
 }

numbers = {1, 2, 6, 8, 9, 11}
def find_sorting(numbers):
    numbers1 = sorted(numbers, key = lambda value: number_names[value])

    return numbers1

res = find_sorting(numbers)
print(" ".join(str(e) for e in res))
