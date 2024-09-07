# Задание 1
# words = ['apple', 'banana', 'cherry', 'date']
# words_list = [x[0] for x in words]
# print(words_list) 


# Задание 2
# num1 = [x**3 for x in range(1, 100)]
# print(num1)


# Задание 3
# num2 = [x**2 for x in range(1, 20) if x % 2 != 0]
# num3 = sum(num2)
# print(num3) 


#Задание 4
#  sentence = 'List comprehensions in Python are powerful'
# wordspl = sentence.split()
# mlenght = max(len(x) for x in wordspl)
# print(mlenght)


# Задание 5
#  numbers = [3, 5, 7, 2, 8]
# min_product = min(numbers[i] * numbers[j] for i in range(len(numbers)) for j in range(i + 1, len(numbers)))
# print(min_product)
# Умножение всех чисел в списке на число, которое больше на 1, потом получение минимального получившегося числа. i это первый множитель взятый из списка, потом за второй множитель берется i + 1. 


# Задание 6
word = input('Введите слово: ')

dict1 = {}

for x in word:
    if x != ' ':
        if x in dict1:
            dict1[x] += 1
        else:
            dict1[x] = 1

for x, count in dict1.items():
    print(f"{x} встречается {count} раз(а)")