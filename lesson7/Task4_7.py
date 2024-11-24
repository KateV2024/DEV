# Необходимо составить список чисел, которые указывают на
# длину слов в строке
# sentence ="thequick brown fox jumps over the lazy dog"
# но только если слово не с  the с обработкой исключения

import re


def word_lengths(sentence):
    words = re.split(r'\s+', sentence)
    word_lengths = []
    for word in words:
        try:
            if word.startswith("the"):
                raise BaseException
            word_lengths.append(len(word))
        except:
                print("the is found")

    return word_lengths

sentence = "thequick brown fox jumps over the lazy dog"
result = word_lengths(sentence)
print(result)