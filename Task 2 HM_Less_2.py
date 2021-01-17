# Задание 2, Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

# user_list = (list(input("Введите данные: ")))
# print(user_list)
# print(len(user_list))
# new_list = 0
# for el in range(int(len(user_list) // 2)):
#     user_list[new_list], user_list[new_list + 1] = user_list[new_list + 1], user_list[new_list]
#     new_list += 2
# print(user_list)

user_list = (list(input("Введите данные: ")))
new_list = user_list[1::2]
# user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2]
print(user_list)
print(new_list)