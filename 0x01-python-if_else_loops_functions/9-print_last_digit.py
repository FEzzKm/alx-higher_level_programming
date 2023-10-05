#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        a = abs(number) % 10
        a = -a
        return a
    else:
        a = number % 10
        return a
