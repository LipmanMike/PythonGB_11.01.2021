user_time_sec = int(input("Введите время в секундах\n>>>"))

hours = user_time_sec // (60 * 60)
minutes = (user_time_sec % (60 * 60)) // 60
sec = (user_time_sec % (60 * 60)) % 60

print(f"Точное время: {hours} : {minutes} : {sec}")