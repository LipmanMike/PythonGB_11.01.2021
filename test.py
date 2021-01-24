# def printname():
#     name = "Mike"
#     # print("Name: ", name)
#     print("locals()", locals()['name'])
#     print(locals())
#
# printname()

# '''Enumerate функция'''
#
# my_list = ('efv', True, None, 435)
# for ind, value in enumerate(my_list, 1):
#     print(ind, value)

# def my_pow(x):
#     return x ** 2 + 10

# data = [1, 2, 3, -5, 7, -8]

# new_list = []
# for i in data:
#     new_list.append(my_pow(i))
# print(new_list)

# result = list(map(my_pow, data))
# print(result)

# def my_filter(x):
#     return x < 0
#
# result = list(filter(my_filter, data))
# print(result)

# def my_name(name, *args):
#     print(name, args)
#
#
# my_name('Mike', 3, 8, 3, 'dfd', 3, )

# def my_name(name, **kwargs):
#     print(name, kwargs)
#
#
# my_name('Mike', age=34, surname='Lypka')

# names = ['Mike', 'Bob', 'Bill']
# ages = [80, 50, 30]
#
# # for names, ages in zip(names, ages):
# #     print(names, ages)
#
# print(dict(zip(names, ages)))

data = [1, 2, 3, -5, 7, -8]
result = list(filter(lambda x: x < 0, data))
print(result)