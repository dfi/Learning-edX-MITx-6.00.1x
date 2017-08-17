#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 02:26:21 2017

@author: sss
"""

## Problem 5 test
#def search(L, e):
#    for i in range(len(L)):
#        if L[i] == e:
#            return True
#        if L[i] > e:
#            return False
#    return False
#
#L = [0, 1, 2, 3]
#e = 1
#
#def newsearch(L, e):
#    size = len(L)
#    for i in range(size):
#        if L[size-i-1] == e:
#            return True
#        if L[i] < e:
#            return False
#    return False



# Problem 6
# 1 这是 merge sort 吗？
def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    count = 0
    for i in range(len(L)):
        print('1-outter-loop')
        for j in range(i+1, len(L)):
            print('(------------1-inner-loop')
            count += 1
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    print('1-count:', str(count))
    

def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    count = 0
    for i in range(len(L)):
        print('Outter loop')
        for j in range(len(L)):
            print('------------Inner loop')
            count += 1
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print('------------', L)
    print("Final L: ", L)
    print('2-count:', str(count))
    
L = [2, 1]
