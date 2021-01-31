# while True:
#     s = input('Введите что-нибудь : ')
#     if s == 'выход':
#         break
#     if len(s) < 3:
#         print('Слишком мало')
#         continue
#     print('Введённая строка достаточной длины') # Разные другие действия здесь...

generator = (param ** 3 for param in range(5))

for el in generator:
    print(el)

# my_set = {el**3 for el in range(5, 10)}
# print((my_set))

# my_list = [i**3 for i in range(5, 10)]
# print(my_list)
# [125, 216, 343, 512, 729]