'''
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку
'''

# for num in range(20, 241):
#     if num % 20 == 0:
#         print(num)
#     elif num % 21 == 0:
#         print(num)

print([x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0])
