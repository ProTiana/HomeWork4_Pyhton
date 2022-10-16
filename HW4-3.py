# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

list = []
for i in range(10):
    list.append(random.randint(1, 10))
print(list)

result = []

count = 0
for i in list:
    if list.count(i) == 1:
        result.append(i)

print(result)