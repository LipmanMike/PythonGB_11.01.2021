from math import factorial
from itertools import count

def fact():
    for n in count(1):
        yield factorial(n)

x = 1
for num in fact():
    print(f"Факториал {x} - {num}")
    if x == 15:
        break
    x += 1

