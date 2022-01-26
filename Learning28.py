# Map, Filter, & Reduce in Python

"""
        The map() function takes two inputs as a function and an iterable object.
        The function that is given to map () is a normal function, and it will
        iterate over all the values present in the iterable object given.

            SYNTAX : - map( function , iterator1, iterator2, iterator3, ...., iterator n)

        iterator : An iterable compulsory object. It can be a list , tuples, etc.

        Return Value : The map() function is going to apply the given functions on all the
        items inside the iterator and return an iterable map object i.e a tuple, a list, etc.
"""

def square(n):
    """
        this function for calculating square of all the numbers.
    """
    return n*n

my_list = [2, 3, 4, 5, 6, 7, 8, 9]
updated_list = map(square, my_list)
print(updated_list, "\n\n")         # Returns object of the given list
print(list(updated_list))           # to get the actual value we need to type-caste it

print(square.__doc__)