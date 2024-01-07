#!/usr/bin/python3
"""A function that replaces an element of a list in a specific position"""


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)

    l = len(my_list)

    if idx > l - 1:
        return(my_list)

    my_list[idx] = element

    return (my_list)
