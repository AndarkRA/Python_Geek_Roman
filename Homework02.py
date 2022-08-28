# Задание 14
# Подсчитать сумму цифр в вещественном числе.

num = input("Введите число с точкой ")
result = 0
for i in range(len(num)):
   if (num[i] == '.'):
       continue
   result += int(num[i])
print(result)

# Задание 15
# -Написать программу получающую набор произведений чисел от 1 до N.

num = int(input())
arr = []
for i in range(0, num + 1):
   if (i == 0):
       arr.append(1)
   else:
       arr.append(arr[i - 1] * (i + 1))
print(arr)

# Задание 18
# Реализовать алгоритм перемешивания списка.

import random
x = list(range(1, 9))
random.shuffle(x)
print(x)