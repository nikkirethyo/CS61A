# CS 61A Summer 2014
# Name: Nichole Rethmeier 
# Login: cs61a-jp

################
# Q1: Scanning #
################

def scan(f, lst, start):
    """Returns a list containing the intermediate values of reducing the list.

    >>> from operator import add, mul
    >>> scan(add, [1, 2, 3, 4], 0)
    [1, 3, 6, 10]
    >>> scan(mul, [3, 2, 1, 0], 10)
    [30, 60, 60, 0]
    """
    accumulated = start 
    def closure(item):
        nonlocal accumulated 
        accumulated = f(accumulated, item)
        return accumulated
    return list(map(closure, lst))


#################################
# Q3: 3..2..1 - Generate Paths! #
#################################

class BST:
    def __init__(self, datum, left=None, right=None):
        self.datum = datum
        self.left = left
        self.right = right

    def paths(self):
        """Return a generator for all of the paths from the root to a leaf.

        >>> tree = BST(5, BST(3, BST(2), BST(4)), BST(10, None, BST(13, BST(12))))
        >>> gen = tree.paths()
        >>> next(gen)
        [5, 3, 2]
        >>> for path in gen:
        ...     print(path)
        ...
        [5, 3, 4]
        [5, 10, 13, 12]
        """
        if not self.right and not self.left:
            yield [self.datum]
        if self.left:
            for path in self.paths(self.left):
                yield [self.datum] + path
        if self.right:
            for path in self.paths(self.right):
                yield [self.datum] + path 

##########################
# Q4: Dealer Always Wins #
##########################

def deal_deck(linked_list, num_of_players):
    """Deals out a deck of cards.

    >>> deck = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6, \
      Link(7, Link(8, Link(9, Link(10))))))))))
    >>> list_of_cards, remainder = deal_deck(deck, 4)
    >>> list_of_cards
    [Link(5, Link(1)), Link(6, Link(2)), Link(7, Link(3)), Link(8, Link(4))]
    >>> remainder
    Link(9, Link(10))
    """
    # Create a list containing each player's hand.
    hands = [Link.empty for i in range(num_of_players)]
    # Give each player the right number of cards.
    for i in range(len(linked_list)//num_of_players):
        # For each player
        for player in range(num_of_players):
            linked_list, card = linked_list.rest, linked_list
            card = first(linked_list)
            hands[player] += card            
    return hands, linked_list

########################
# Predefined Functions #
########################

class Link:
    """A recursive list, with Python integration."""
    empty = None

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + repr(self.rest)
        return 'Link({}{})'.format(self.first, rest)

    def __str__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ' ' + str(self.rest)[2:-2]
        return '< {}{} >'.format(self.first, rest)

    def __len__(self):
        if self.rest is Link.empty:
            return 1
        return 1 + len(self.rest)  # self.rest.__len__()

    def __getitem__(self, index):
        if index == 0:
            return self.first
        elif self.rest is Link.empty:
            raise IndexError
        return self.rest[index - 1]  # self.rest.__getitem__(index - 1)


