# Construct an iterator from those elements of iterable for which function is true.
# iterable may be either a sequence, a container which supports iteration, or an iterator.
# If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.

# Note that filter(function, iterable) is equivalent to the generator expression
# (item for item in iterable if function(item)) if function is not None and (item for item in iterable if item) if function is None.
from colorama import Fore


class ft_filter:
    """filter(function or None, iterable) --> filter object\n\nReturn an iterator yielding those items of iterable for which function(item)\nis true. If function is None, return the items that are true."""

    def __init__(self, func, iterable):
        # store function and iterable
        self.func = func
        self.iterable = iterable
        self.filtered_element = iterable
        self.index = 0
        # set __name__ attribute
        self.__name__ = "filter"

    def __iter__(self):
        # iterable behavior
        # filter elements of iterable using function
        self.filtered_elements = [item for item in self.iterable if self.func(item)]
        self.index = 0
        return self

    def __next__(self):
        # called on return object of __iter__
        if self.index < len(self.filtered_elements):
            result = self.filtered_elements[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
