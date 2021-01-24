'''Реализовать функцию my_func(),которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
'''
def my_func(num_1, num_2, num_3):
    list_number = [num_1, num_2, num_3]
    list_number.pop(list_number.index(min(num_1, num_2, num_3)))
    print(list_number)
    sum_max = sum(list_number)
    return sum_max


print(my_func(2, 9, 3))



