'''
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
'''

original_list = [1, 975, 34, 212, 555, 54, 234, 102324, 4, 211]
for i in range(1, len(original_list)):
    if original_list[i] > original_list[i - 1]:
        print(original_list[i])

# original_list = [1, 975, 34, 212, 555, 54, 234, 102324, 4, 211]
# new_list = [num for i, num in enumerate(original_list) if num > original_list[i - 1] and i != 0]
# print(new_list)

