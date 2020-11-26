"""This module contains  the bisect example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""


def recursive_polynomial(a_list, x):
    if len(a_list) == 0:
        return 0
    else:
        return a_list[0] * x ** (len(a_list) - 1) + recursive_polynomial(a_list[1:], x)


def in_bisect(a_list, an_element):
    """Checks whether an element is in a list using bisection search.

    Precondition: the elements in the list are sorted

    returns: True if the word is in the list; False otherwise
    """
    if len(a_list) == 0:
        return False

    i = len(a_list) // 2
    if a_list[i] == an_element:
        return True
    elif a_list[i] > an_element:
        # search the first half
        return in_bisect(a_list[:i], an_element)
    else:
        # search the second half
        return in_bisect(a_list[i + 1:], an_element)


def index_bisect(a_list, an_element):
    """Checks whether a an_element is in a list using bisection search.

    Precondition: the list is sorted

    a_list: list
    an_element: a new element

    returns: An index into the sorted list, where an_element can be inserted
    """
    if len(a_list) == 0:
        return 0

    i = len(a_list) // 2
    if a_list[i] == an_element:
        return i
    elif a_list[i] > an_element:
        # search the first half
        return index_bisect(a_list[:i], an_element)
    else:
        # search the second half
        return i + 1 + index_bisect(a_list[i + 1:], an_element)


def insort_bisect(a_list, a_element):
    insertion_index = index_bisect(a_list, a_element)
    a_list.insert(insertion_index, a_element)


def neg_pos(l):
    #print("neg_pos({})".format(l))
    if l == []:
        return True
    else:
        return l[0] <= 0 and pos_neg(l[1:])


def pos_neg(l):
    #print("pos_neg({})".format(l))
    if l == []:
        return True
    else:
        return l[0] >=0 and neg_pos(l[1:])


def alternating_sequence(l):
    return pos_neg(l) or neg_pos(l)


class Lucas:

    def __init__(self, x0, x1):
        self.known = {0: x0, 1: x1}
        self.counter = 0

    def reset(self):
        self.counter = 0
        self.known = {0: self.known[0], 1: self.known[1]}

    def get_counter(self):
        return self.counter

    def solve(self, n):
        if n in self.known:
            return self.known[n]
        self.counter += 1
        return self.solve(n - 1) + self.solve(n - 2)

    def solve_memoized(self, n):

        if n in self.known:
            return self.known[n]
        self.counter += 1
        res = self.solve_memoized(n - 1) + self.solve_memoized(n - 2)
        self.known[n] = res
        return res



