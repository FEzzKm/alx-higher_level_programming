#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    Args:
        my_list (list): list to print elements from.
        x (int): number of elements of my_list to print.
    Returns:
        number of elements printed.
    """

    a = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end="")
            a += 1
        except IndexError:
            break
    print("")
    return(a)
