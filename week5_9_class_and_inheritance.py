#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:27:00 2017

@author: sss
"""

#class Clock(object):
#    def __init__(self, time):
#        self.time = time
#    def print_time(self):
#        time = '6:30'
#        print(self.time)
#        
#clock = Clock('5:30')
#clock.print_time()

#class Clock(object):
#    def __init__(self, time):
#        self.time = time
#    def print_time(self, time):
#        print(time)
#        
#clock = Clock('5:30')
#clock.print_time('10:30')

#class Clock(object):
#    def __init__(self, time):
#        self.time = time
#    def print_time(self):
#        print(self.time)
#    def get_time(self):
#        return self.time
#        
#boston_clock = Clock('5:30')
#paris_clock = boston_clock
#paris_clock.time = '10:30'
#boston_clock.print_time()

#class Coordinate(object):
#    def __init__(self,x,y):
#        self.x = x
#        self.y = y
#
#    def getX(self):
#        # Getter method for a Coordinate object's x coordinate.
#        # Getter methods are better practice than just accessing an attribute directly
#        return self.x
#
#    def getY(self):
#        # Getter method for a Coordinate object's y coordinate
#        return self.y
#
#    def __str__(self):
#        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
#        
#    def __eq__(self, other):
#        return self.x == other.x and self.y == other.y
#        
#    def __repr__(self):
#        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + \
#                            ')'

#==============================================================================
# class intSet(object):
#     """An intSet is a set of integers
#     The value is represented by a list of ints, self.vals.
#     Each int in the set occurs in self.vals exactly once."""
# 
#     def __init__(self):
#         """Create an empty set of integers"""
#         self.vals = []
# 
#     def insert(self, e):
#         """Assumes e is an integer and inserts e into self""" 
#         if not e in self.vals:
#             self.vals.append(e)
# 
#     def member(self, e):
#         """Assumes e is an integer
#            Returns True if e is in self, and False otherwise"""
#         return e in self.vals
# 
#     def remove(self, e):
#         """Assumes e is an integer and removes e from self
#            Raises ValueError if e is not in self"""
#         try:
#             self.vals.remove(e)
#         except:
#             raise ValueError(str(e) + ' not found')
# 
#     def __str__(self):
#         """Returns a string representation of self"""
#         self.vals.sort()
#         return '{' + ','.join([str(e) for e in self.vals]) + '}'        
#     def intersect(self, other):
#         temp = intSet()
#         for e in self.vals:
#             if e in other.vals:
#                 temp.insert(e)
#         return temp
#     def __len__(self):
#         return len(self.vals)
# 
# a = intSet()
# b = intSet()
# a.insert('a')
# a.insert('aa')
# a.insert('aaa')
# b.insert('b')
# b.insert('bb')
# b.insert('bbb')
# a.insert('c')
# a.insert('cc')
# a.insert('ccc')
# b.insert('c')
# b.insert('cc')
# b.insert('ccc')
#==============================================================================

# E4
class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")