#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        iterator = iter(my_list)
        for _ in range(x):
            element = next(iterator)
            if type(element) == int:
                print("{:d}".format(element), end="")
                count += 1
    except StopIteration:
        pass
    finally:
        print()
        return count
