
'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
'''

from functools import reduce, partial

def my_func(num1, num2):
    return num1 * num2

my_list = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(my_func, my_list))