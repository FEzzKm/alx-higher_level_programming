#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list """
    r = 0
    for x in set(my_list):
        r += x
    return (r)
