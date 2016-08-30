# CS 61A Summer 2014
# Name: Nichole Rethmeier
# Login: cs61a-jp 

############
# Nonlocal #
############

def make_accumulator():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    total = []
    def accumulate(arg): 
        acc = 0
        total.append(arg)
        for i in total: 
            acc += i
        return acc 
    return accumulate

def make_accumulator_nonlocal():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator_nonlocal()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator_nonlocal()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    total = 0 
    def accumulator(arg):
        nonlocal total 
        total += arg 
        return total 
    return accumulator


#######
# OOP #
#######

class Amount(object):
    """An amount of nickels and pennies.

    >>> a = Amount(3, 7)
    >>> a.nickels
    3
    >>> a.pennies
    7
    >>> a.value
    22
    >>> a.nickels = 5
    >>> a.value
    32

    """
    def __init__ (self, x, y):
        self.nickels = x 
        self.pennies = y

    @property
    def value(self):
        return self.nickels * 5 + self.pennies
    
    def nickels(self):
        return self.nickels  

    
    def pennies(self):
        return self.pennies


class MinimalAmount(Amount):
    """An amount of nickels and pennies that is initialized with no more than
    four pennies, by converting excess pennies to nickels.

    >>> a = MinimalAmount(3, 7)
    >>> a.nickels, a.pennies, a.value  # Creates a tuple
    (4, 2, 22)
    >>> a = MinimalAmount(7, 3)
    >>> a.nickels, a.pennies, a.value
    (7, 3, 38)
    >>> a = MinimalAmount(0, 50)
    >>> a.nickels, a.pennies, a.value
    (10, 0, 50)
    """
    def __init__(self, x, y):
        self.nickels =  x 
        self.pennies = y 
        while self.pennies > 4:
            if self.pennies > 4: 
                self.pennies -= 5
                self.nickels += 1



    

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(1)
    'Current candy stock: 1'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.restock(1)
    'Current candy stock: 2'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.vend()
    'Machine is out of stock.'
    >>> p = VendingMachine('pepsi', 21)
    >>> p.restock(100)
    'Current pepsi stock: 100'
    >>> p.deposit(100)
    'Current balance: $100'
    >>> p.vend()
    'Here is your pepsi and $79 change.'
    >>> p.deposit(21)
    'Current balance: $21'
    >>> p.vend()
    'Here is your pepsi.'
    """

    def __init__(self, item, price):
        self.item = item 
        self.price = price 
        self.quantity = 0
        self.balance = 0 
        self.stock = 0 

    def restock(self, quantity): 
        self.stock += quantity
        return 'Current {0} stock: {1}'.format(self.item, self.stock)

    def deposit(self, money):
        self.balance += money 
        if self.stock == 0: 
            return "Machine is out of stock. Here is your ${0}.".format(money)
        else: 
            return 'Current balance: ${0}'.format(self.balance)

    
    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.balance < self.price: 
            deficit = self.price - self.balance
            return 'You must deposit ${0} more.'.format(deficit)
        elif self.balance == self.price: 
            self.stock -= 1
            self.balance -= self.price 
            return 'Here is your {0}.'.format(self.item)
        elif self.balance > self.price: 
            self.stock -= 1
            change = self.balance - self.price
            self.balance = 0
            return 'Here is your {0} and ${1} change.'.format(self.item, change)


class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    """
    def __init__(self, vendingmach): 
        self.VendingMachine = vendingmach

    def ask(self, string, *args):
        if 'please' in string: 
            if 'vend' in string: 
                getattr(VendingMachine, 'vend')
            elif 'deposit'in string: 
                getattr(VendingMachine, 'deposit')
            else: 
                string = string[len(' please'):]
                return "Thanks for asking, but I know not how to {}".format(string)
        else: 
            return "You must learn to say please first."


# ############
# # Optional #
# ############

# def make_withdraw(balance, password):
#     """Return a password-protected withdraw function.

#     >>> w = make_withdraw(100, 'hax0r')
#     >>> w(25, 'hax0r')
#     75
#     >>> w(90, 'hax0r')
#     'Insufficient funds'
#     >>> w(25, 'hwat')
#     'Incorrect password'
#     >>> w(25, 'hax0r')
#     50
#     >>> w(75, 'a')
#     'Incorrect password'
#     >>> w(10, 'hax0r')
#     40
#     >>> w(20, 'n00b')
#     'Incorrect password'
#     >>> w(10, 'hax0r')
#     "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
#     >>> w(10, 'l33t')
#     "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
#     """
#     "*** YOUR CODE HERE ***"

# # Old version
# def count_change(a, coins=(50, 25, 10, 5, 1)):
#     if a == 0:
#         return 1
#     elif a < 0 or len(coins) == 0:
#         return 0
#     return count_change(a, coins[1:]) + count_change(a - coins[0], coins)

# # Version 2.0
# def make_count_change():
#     """Return a function to efficiently count the number of ways to make
#     change.

#     >>> cc = make_count_change()
#     >>> cc(500, (50, 25, 10, 5, 1))
#     59576
#     """
#     "*** YOUR CODE HERE ***"


