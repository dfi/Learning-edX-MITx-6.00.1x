#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 21:47:28 2017

@author: sss
"""

#def program1(x):
#    total = 0
#    for i in range(1000):
#        total += 1
#        
#    return total
#
#c = 10
#n = 10000
#print(c**n > n**c)

#def foo(L):
#    val = L[0]
#    while True:
#        val = L[val]
#        
#a = [1, 2, 3, 4, 0]
#b = [3, 0, 2, 4, 1]
#c = [3, 2, 4, 1, 5]

#def search3(L, e):
#    try:
#        if L[0] == e:
#            return True
#        elif L[0] > e:
#            return False
#        else:
#            return search3(L[1:], e)
#    except IndexError:
#        return False
#
#L = [1, 2, 3, 4]
#e = 5

# My Bubble Sort
def my_bubble_sort(L):
    if len(L) == 0 or len(L) == 1:
        return L
    while True:
        swap_occurred = False
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                swap_occurred = True
        if swap_occurred == False:
            break
L = [1, 3, 5, 0, 9, 11, 2, 4]   


## My Selection Sort
## 没写出来
##def my_selection_sort(L):
##    if len(L) == 0 or len(L) == 1:
##        return L
##    min_e = L[0]
##    for i in range(len(L)):
##        if L[i] < min_e:
##            min_e = L[i]
##    return 
#
# edX's selection sort
def edx_selection_sort(L):
    suffix = 0
    while suffix != len(L):
        for i in range(suffix, len(L)):
            if L[i] < L[suffix]:
                L[suffix], L[i] = L[i], L[suffix]
        suffix += 1

# 12. Searching and Sorting Algorithms. Exercise 6
def mySort(L):
    ''' L, list with unique elements '''
    clear = False
    examined_count = 0
    while not clear:
        clear = True
        for j in range(1, len(L)):
            print('mySort examined once.')
            examined_count += 1
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    print('mySort examined', examined_count)
                
def newSort(L):
    ''' L, list with unique elements '''
    examined_count = 0
    for i in range(len(L) - 1):
        j = i + 1
        while j < len(L):
            print('newSort examined once.')
            examined_count += 1
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
    print('newSort examined', examined_count)
            
L1 = [2, 4, 3, 7, 8, 0, 9, 11]
L2 = [2, 4, 3, 7, 8, 0, 9, 11]
L3 = [1, 2, 3]
L4 = [1, 2, 3]
L5 = [3, 2, 1]
L6 = [3, 2, 1]