
from itertools import count, cycle
#
# for i in count(int(input('Введите целое исло: '))):
#     print(i)

my_list = [1, 2, 3, 4, 5, 6, 77, 8, 443, 456]
iter = cycle(my_list)
stop = ''
while stop != 'q':
    print(next(iter), end='')
    stop = input()



