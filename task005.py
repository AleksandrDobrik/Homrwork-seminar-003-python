
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: fn = fn-1 + fn-2
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

n = int(input('Enter number '))
fib = [0]
count = 0

for i in range(n*2):
    fib.append(0)

while( count < n):
    count += 1
    if count == 1 or count == 2:
        fib[n + count] = 1 
        fib[n - count] = 1 * (-1) ** (count + 1)
    if count > 2:
        fib[n + count] = (fib[n + count - 1] + fib[n + count - 2] ) 
        fib[n - count] = fib[n + count] * (-1) ** (count + 1)

print(fib)