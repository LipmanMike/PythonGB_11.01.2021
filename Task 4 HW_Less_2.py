# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_message = input('Введите сообщение: ')
user_message = user_message.split()
for number, message in enumerate(user_message):
    print(number, message[:10])


