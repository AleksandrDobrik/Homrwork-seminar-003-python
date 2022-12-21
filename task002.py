# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint as RI
import math
n = int(input('Enter size list '))
my_list = []
end_list = []
sum = 0

for i in range(n):
    my_list.append(RI(0,10))
print(my_list)

for i in range(math.ceil(len(my_list)/2)):
    end_list.append (my_list[i] * my_list[-i-1])
print(end_list)

