#!/usr/bin/python3
""" The list module """


class MyList(list):
    """ A class that inherits from the list """
    def print_sorted(self):
        """ The function prints the sorted list in ascending order """
        self.sort()
        print(self)

