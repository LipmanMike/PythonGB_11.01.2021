''' Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
'''
# name, surname, birth, city, email, tel
# def user(name, surname, birth, city, email, tel):
    # user_info = {
    #     'name': '',
    #     'surname': '',
    #     'birth': '',
    #     'city': '',
    #     'email': '',
    #     'tel': '',
    # }
#     for k in user_info.keys():
#         user_data = input

    # user_name = input('Введите имя: ')
    # user_surname = input('Введите фамилию: ')
    # user_birth = input('Введите дату рождения: ')
    # user_city = input('Введите город проживания: ')
    # user_email = input('Введите email: ')
    # user_tel = input('Введите номер телефона: ')
#
# def user_info(**kwargs):
#     return kwargs
#     # print(user_info)

def user(name, surname, birth, city, email, tel):
    print(locals())

user('Mike', 'Lypka', '25.02.1985', 'Yalta', 'lypka@gmail', '+744353')