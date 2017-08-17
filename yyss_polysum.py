#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:23:25 2017

This .py file is made during my edX online practice:
Week 2: Simple Programs > Complete Programming Experience: polysum > Grader
MITx: 6.00.1x Introduction to Computer Science and Programming Using Python

See more at:
https://courses.edx.org/courses/course-v1:MITx+6.00.1x_11+1T2017/
    
@author: sss
"""

# my polysum function
def polysum(n, s):
    
    '''
    n: number of sides of a regular polygon
    s: length of each side
    
    returns: the sum of area and square of the perimeter of the 
             regular polygon, rounded to 4 decimal places.

    '''
    
    # The number of sides should be an int. 
    if not isinstance(n, int):
        print(str(n) + ' is not an int, please try again.')
        return
    
    # The length of each side should be an int or float.
    if not isinstance(s, (int, float)):
        print(str(s) + ' is not a float, please try again.')
        return
    
    # Check if the regular polygon has at least 3 sides 
    # and each side's length is larger than 0.
    # Return 0 if not.
    if n <= 2 or s <= 0:
        return 0
    
    # Now the calculation begins.
    # First we need `tan` and `pi` from `math`.
    from math import tan, pi
    
    # The area of regular polygon is: (0.25*n*s^2)/tan(pi/n).
    area = (0.25 * n * s * s) / tan(pi / n)
    
    # The perimeter of a polygon is: length of the boundary of the polygon.
    perimeter = n * s
    
    return round(area + perimeter * perimeter, 4)