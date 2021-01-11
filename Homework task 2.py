user_number1 = input("Введите число\n>>> ")
user_number2 = input("Введите еще одно число\n>>> ")
user_number1 = int(user_number1)
user_number2 = int(user_number2)
user_numbers_summ = user_number1 + user_number2
user_message1 = input("Введите сообщение\n>>> ")
user_message2 = input("Введите еще одно сообщение\n>>> ")

print(f"Вы вводили числа: '{user_number1}' '{user_number2}'\nСумма введенных чисел равна {user_numbers_summ}")
print(f"Вы вводили следующие сообщения:\n'{user_message1}' \n'{user_message2}'")