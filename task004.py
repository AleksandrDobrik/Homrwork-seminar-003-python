# ; Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# ; Пример:
# ; 45 -> 101101
# ; 3 -> 11
# ; 2 -> 10

n = int(input('Enter integer number '))
number_binary = []

while(n != 0):
    number_binary.append(n % 2)
    n //= 2 

for i in range(len(number_binary) - 1, -1, -1):
    print(number_binary[i], end = '')