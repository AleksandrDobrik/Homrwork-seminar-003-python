# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as RI

n = int(input('Enter size list '))
my_list = []
sum = 0

for i in range(n):
    my_list.append(RI(0,10))
print(my_list)

for i in range(1,n,2):
    sum += my_list[i]
print(sum)