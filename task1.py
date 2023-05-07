# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8
def fibonacci():
    fib1 = fib2 = 1
    N = int(input("Введите количество элементов: "))
    print(fib1, fib2, end=' ')

    for i in range(2, N):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')





fibonacci()