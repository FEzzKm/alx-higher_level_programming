#!/usr/bin/python3

"""Function that removes all c and C from string"""


def no_c(my_string):
    st_len = len(my_string)

    i = 0
    nw_st = my_string[:]

    for char in range(st_len):
        if (my_string[char] == 'c' or my_string[char] == 'C'):
            nw_st = nw_st[:(char - i)] + my_string[(char + 1):]
            i += 1

    return (nw_st)
