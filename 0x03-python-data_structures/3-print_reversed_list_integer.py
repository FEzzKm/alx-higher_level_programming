#!/usr/bin/python3
""" function that prints int in reverse"""


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
       n = len(my_list) - 1

       while n >= 0:
            print("{:d}".format(my_list[n]))
            n -= 1
