#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    a = 10
    b = 5
    summ = add(a, b)
    subt = sub(a, b)
    mult = mul(a, b)
    divi = div(a, b)
    print("{} + {} = {}".format(a, b, summ))
    print("{} + {} = {}".format(a, b, subt))
    print("{} + {} = {}".format(a, b, mult))
    print("{} + {} = {}".format(a, b, divi))
