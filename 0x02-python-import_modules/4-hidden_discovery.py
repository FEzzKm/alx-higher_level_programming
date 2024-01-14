#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    a = dir(hidden_4)
    for b in a:
        if b[:2] != "__":
            print(b)
