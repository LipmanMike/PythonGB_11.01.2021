# Задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

user_month = int(input('Введите номер месяца: '))
if user_month in winter:
    print(f'{user_month} это зима')
elif user_month in spring:
    print(f'{user_month} это весна')
elif user_month in summer:
    print(f'{user_month} это лето')
elif user_month in autumn:
    print(f'{user_month} это осень')

# Как сделать так чтобы программа выводила не номер месяца и пору года, а название месяца и пору года?