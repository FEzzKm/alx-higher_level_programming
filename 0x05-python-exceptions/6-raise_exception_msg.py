#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raise a TypeError exception with msg."""
    raise NameError(message)

try:
    raise TypeError
except NameError as e:
        print(f"Caught an exception: {e}")
