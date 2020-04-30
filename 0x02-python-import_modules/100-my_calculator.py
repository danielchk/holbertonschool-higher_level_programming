#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    count = len(argv)
    if count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    calc = argv[2]
    if calc == "+":
        num = add(a, b)
    elif calc == "-":
        num = sub(a, b)
    elif calc == "*":
        num = mul(a, b)
    elif calc == "/":
        num = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
    print("{:d} {} {:d} = {:d}".format(a, calc, b, num))
