#!/usr/bin/python3
""" fct prints ints in reverse"""


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
       a = len(my_list) - 1

       while a >= 0:
            print("{:d}".format(my_list[a]))
            a -= 1
