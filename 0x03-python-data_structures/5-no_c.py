#!/usr/bin/python3

"""Function removes c and C from string"""


def no_c(my_string):
    string_length = len(my_string)

    i = 0
    ns = my_string[:]

    for char in range(string_length):
        if (my_string[char] == 'c' or my_string[char] == 'C'):
            ns = new_string[:(char - i)] + my_string[(char + 1):]
            i += 1

    return (ns)
