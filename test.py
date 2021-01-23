# def printname():
#     name = "Mike"
#     # print("Name: ", name)
#     print("locals()", locals()['name'])
#     print(locals())
#
# printname()

'''Enumerate функция'''


# my_list = ['efv', True, None, 435]
# for value, ind in enumerate(my_list, 1):
#     print(ind, value)

def my_pow(x):
    return x ** 2 + 10

data = [1, 2, 3, 5, 7, 8]

new_list = []
for i in data:
    new_list.append(my_pow(i))
print(new_list)
