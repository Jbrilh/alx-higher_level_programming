#!/usr/bin/python3
import sys
if __name__ == '__main__':
    arguments = sys.argv[1:]
    num_arguments = len(arguments)
    if num_arguments == 0:
        print("{} arguments:".format(0))
    elif num_arguments == 1:
        print("{} argument:".format(1))
    else:
        print("{} arguments:".format(num_arguments))
    for i, arg in enumerate(arguments):
        print("{}: {}".format(i + 1, arg))
