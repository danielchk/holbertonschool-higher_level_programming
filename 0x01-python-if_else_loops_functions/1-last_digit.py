#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    res = (number % -10)
else:
    res = (number % 10)
print("Last digit of {:d} is {:d}".format(number, res), end=" ")
if res == 0:
    print("and is 0")
elif res > 5:
    print("and is greater than 5")
else:
    print("and is lessf than 6 and not 0")
