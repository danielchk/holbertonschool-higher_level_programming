#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    res = (number % -10)
else:
    res = (number % 10)
print("Last digist of", number, "is", res, end=' ')

if res == 0:
    print("and is 0")
elif res > 5:
    print("and is greater than 5")
else:
    print("and is les than 6 and not 0")
