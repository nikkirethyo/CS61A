# Q3

def f1():
    """
    >>> f1()
    3
    """
    return 3

def f2():
    """
    >>> f2()()
    3
    """
    return lambda: 3

def f3():
    """
    >>> f3()(3)
    3
    """
    return lambda x: 3

def f4():
    """
    >>> f4()()()
    3
    """
    return lambda: lambda: 3

def f5():
    """
    >>> f5()()(3)()
    3
    """
    return lambda: lambda x: lambda: 3


#Q5

def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.
    
    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    def print_number(x): 
        k = 0
        while k < x:
            if k % n == 0: 
                print('Buzz!')
            else:
                print(k) 
            k += 1   
    return print_number


    # Q6

def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    ...
    >>> def times2(x):
    ...     return x * 2
    ...
    >>> def add3(x):
    ...     return x + 3
    ...
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def times_thru_cycle(n):
        def final_func(x): 
            counter = n            
            if counter == 0: 
                return x
            elif counter % 3 == 1:
                return f1(times_thru_cycle(counter - 1)(x))
            elif counter % 3 == 2:
                return f2(times_thru_cycle(counter - 1)(x))
            elif counter % 3 == 0:
                return f3(times_thru_cycle(counter - 1)(x))
        return final_func
    return times_thru_cycle       

# Functional representation of pairs

def cons(a, b):
    def answer(m):
        if m == 'car':
            return a
        else:
            return b
    return answer

def car(p):
    return p('car')

def cdr(p):
    return p('cdr')


# Implementation of linked lists using cons

empty = lambda: 42

def link(element, list):
    return cons(element, list)

def first(list):
    return car(list)

def rest(list):
    return cdr(list)

def print_linked_list(list):
    s = '<'
    while list != empty:
        s = s + repr(first(list)) + ' '
        list = rest(list)
    return s[:-1] + '>'
        

# Q7

def sum_linked_list(lst, term):
    """ Applies a function TERM to each number in LST and returns the sum
    of the resulting values

    >>> square = lambda x: x*x
    >>> double = lambda y: 2*y
    >>> lst1 = link(1, link(2, link(3, link(4, empty))))    
    >>> sum_linked_list(lst1, square)
    30
    >>> lst2 = link(3, link(5, link(4, link(10, empty))))
    >>> sum_linked_list(lst2, double)
    44
    """
    if lst == empty:
        return 0 
    else: 
        return term(first(lst)) + sum_linked_list(rest(lst), term)

