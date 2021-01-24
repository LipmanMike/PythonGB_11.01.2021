def amount():
    stop = False
    sum_total = 0
    while stop == False:
        user_numbers = input('нажмите Enter для ввод числа или q для выхода: ').split()
        temp_numbers = 0
        for num in user_numbers:
            if 'q' in num:
                stop = True
                break
            temp_numbers += int(num)
        sum_total += temp_numbers
    # return sum_total
    print(f'Сумма введенных чисел равна {sum_total}')

amount()
