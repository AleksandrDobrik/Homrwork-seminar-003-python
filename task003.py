# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = int(input('Enter size list '))
my_list = []


for i in range(n):
    comma = random.randint(0,3)
    my_list.append(round (random.uniform(0,10), comma))
print(my_list)

maximum_balance = 0
minimum_balance = 1

for i in range(len(my_list)):
    if my_list[i] - int(my_list[i]) != 0:
        balannce = round(my_list[i] - int(my_list[i]),3)
        if balannce > maximum_balance:
            maximum_balance = balannce    
        if balannce < minimum_balance:
            minimum_balance = balannce

         
if maximum_balance !=0:
    print(maximum_balance - minimum_balance)
else:
    print('All numbers are integer ')

