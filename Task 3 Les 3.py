'''Реализовать функцию my_func(),которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
'''
def my_func(num_1, num_2, num_3):
    sum_max = max(num_1, num_2, num_3)
    my_func()
    return sum_max

print(my_func(1, 7, 3))
