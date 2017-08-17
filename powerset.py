#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:19:25 2017

@author: sss
"""

# Powerset generator in Python
# https://www.technomancy.org/python/powerset-generator-python/

from functools import reduce
from itertools import chain, combinations

def powerset(seq):
    '''
    Returns all the subsets of this set. This is a generator.
    '''
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

# Another powerset methods set
# https://rosettacode.org/wiki/Power_set#Python
def list_powerset(lst):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in lst:
        # for every additional element in our set
        # the power set consists of the subsets that don't
        # contain this element (just take the previous power set)
        # plus the subsets that do contain the element (use list
        # comprehension to add [x] onto everything in the
        # previous power set)
        result.extend([subset + [x] for subset in result])
    return result

# the above function in one statement
def list_powerset2(lst):
    return reduce(lambda result, x: result + [subset + [x] for subset in result],
                  lst, [[]])

def powerset3(s):
    return frozenset(map(frozenset, list_powerset(list(s))))


# using itertools
# http://stackoverflow.com/questions/18035595/powersets-in-python-using-itertools
def iter_powerset(iterable):
    s = list(iterable)
    result = chain.from_iterable(combinations(s,r) for r in range(len(s)+1))
    return list(result)


L = [1, 2 ,3 ,4]