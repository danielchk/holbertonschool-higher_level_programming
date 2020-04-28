#!/usr/bin/python3
def fizzbuzz():
    for div in range(1, 101):
        if div % 15 == 0:
            print("FizzBuzz", end=" ")
        elif div % 3 == 0:
            print("Fizz", end=" ")
        elif div % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(div), end=" ")
