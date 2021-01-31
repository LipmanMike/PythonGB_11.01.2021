# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new_list = set(my_list)
# new_list = list(new_list)
# print(new_list)

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = []
# def not_repeat_generator():
#     for num in my_list:
#         if num not in new_list:
#             new_list.append(num)
#             yield num
# orig_list = not_repeat_generator()
#
# for num in orig_list:
#     print(num)


# for num in my_list:
#     if num not in new_list:
#         new_list.append(num)
#
# print(new_list)

original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [x for x in original_list if original_list.count(x) == 1]
print(new_list)
