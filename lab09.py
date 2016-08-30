#############
# Iterators #
#############

class AnIterator(object):
    def __init__(self):
        self.current = 0
    def __next__(self):
        if self.current >= 5:
            raise StopIteration
        result = self.current
        self.current += 1
        return result
    def __iter__(self):
        return self

class IteratorA(object):
    def __init__(self):
        self.start = 5

    def __next__(self):
        if self.start == 100:
            raise StopIteration
        self.start += 5
        return self.start

    def __iter__(self):
        return self

class IteratorB(object):
    def __init__(self):
        self.start = 5

    def __iter__(self):
        return self

class IteratorC(object):
    def __init__(self):
        self.start = 5

    def __next__(self):
        if self.start == 10:
            raise StopIteration
        self.start += 1
        return self.start

class IteratorD(object):
    def __init__(self):
        self.start = 1

    def __next__(self):
        self.start += 1
        return self.start

    def __iter__(self):
        return self


class IteratorRestart(object):
    """
    >>> i = IteratorRestart(2, 6)
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    """
    def __init__(self, start, end):
        self.start = start 
        self.end = end

    def __next__(self):
        result = self.start
        if result == self.end: 
            self.start = 2
            raise StopIteration 
            return IteratorRestart
        self.start += 1 
        return result

    def __iter__(self):
        return self 


##############
# Generators #
##############

def countdown(n):
    """
    >>> for number in countdown(3):
    ...     print(number)
    ...
    3
    2
    1
    0
    """
    start = n 
    while n >= 0:
        yield n 
        n -= 1

class Countdown(object):
    """
    >>> counter = Countdown(3)
    >>> hasattr(counter, '__next__')
    False
    >>> for number in counter:
    ...     print(number)
    ...
    3
    2
    1
    0
    """
    def __init__(self, start): 
        self.start = start 

    def __iter__(self):
        while self.start >= 0:
            yield self.start
            self.start -= 1

def hailstone(n):
    """
    >>> type(hailstone(10))
    <class 'generator'>
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    start = n 
    yield start
    while start > 1: 
        if start % 2 == 0: 
            result = start // 2
            yield result
        else: 
            result = start * 3 + 1
            yield result
        start = result

def pairs(lst):
    """
    >>> type(pairs([3, 4, 5]))
    <class 'generator'>
    >>> for x, y in pairs([3, 4, 5]):
    ...     print(x, y)
    ...
    3 3
    3 4
    3 5
    4 3
    4 4
    4 5
    5 3
    5 4
    5 5
    """
    for i in range(len(lst)):   
        for items in lst:

            yield (lst[i], items)


# ############
# # Optional #
# ############

# class PairsIterator:
#     """
#     >>> for x, y in PairsIterator([3, 4, 5]):
#     ...     print(x, y)
#     ...
#     3 3
#     3 4
#     3 5
#     4 3
#     4 4
#     4 5
#     5 3
#     5 4
#     5 5
#     """
#     def __init__(self, lst):
#         "*** YOUR CODE HERE ***"

#     def __next__(self):
#         "*** YOUR CODE HERE ***"

#     def __iter__(self):
#         "*** YOUR CODE HERE ***"

