#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last = number % 10
else:
    last = (number * -1) % 10 * -1
message = f"Last digit of {number} is {last} and "
if last > 5:
    print(f"{message}is greater than 5")
elif last == 0:
    print(f"{message}is 0")
elif last < -6 and last != 0:
    print(f"{message}is less than 6 and not 0")
