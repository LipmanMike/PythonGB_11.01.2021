distance_a = 3 # расстояние в первый день
distance_b = 15 # расстояние в крайний день
day = 1
while distance_a <= distance_b:
    print(f"День {day}, расстояние: {round(distance_a, 2)} км")
    distance_a = distance_a * 0.1 + distance_a
    day += 1
if distance_a > distance_b:
    day += 1
    print(f"Спортсмен достиг результата на {day} день - пробежал на менее {day} км")