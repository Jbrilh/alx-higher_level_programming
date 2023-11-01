#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("{}".format("FizzBuzz"), end=", ")
        if i % 3 == 0:
            print("{}".format("Fizz"), end=", ")
            continue
        if i % 5 == 0:
            print("{}".format("Buzz"), end=", ")
            continue
        print("{:d}".format(i), end=", ")
    print("{}".format("Buzz"), end=" ")
