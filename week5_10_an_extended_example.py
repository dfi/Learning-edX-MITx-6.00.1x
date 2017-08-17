#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 22:49:42 2017

@author: sss
"""

def genPrimes():
    all_primes = [2]
    next_guess = all_primes[-1]
    yield next_guess
    while True:
        next_guess += 1
        for i in all_primes:
            if next_guess % i == 0:
                break  
        else:
            all_primes.append(next_guess)
            yield next_guess


#def genPrimes():
#  primeL=[2]
#  test=3
#  while True:
#    passed=True
#    for p in primeL:
#     if test%p==0:
#       passed=False
#       break
#    if passed:
#      yield primeL[-1]
#      primeL.append(test)
#    test+=2


#def genPrimesFn():
#    '''Function to keep printing the prime number until the user stops the program.
#    This way uses user input; you can also just run an infinite loop (while True)
#    that the user can quit out of by hitting control-c'''
#    primes = []   # primes generated so far
#    last = 1      # last number tried
#    uinp = 'y'    # Assume we want to at least print the first prime...
#    while uinp != 'n':
#        last += 1
#        for p in primes:
#            if last % p == 0:
#                break
#        else:
#            primes.append(last)
#            print(last)
#            uinp = input("Print the next prime? [y/n] ")
#            while uinp != 'y' and uinp != 'n':
#                while uinp:
#                    print("Sorry, I did not understand your input. Please enter 'y' for yes, or 'n' for no.")
#                    uinp = input("Print the next prime? [y/n] ")
#            if uinp == 'n':
#                break

#def isThisGenerator():
#    if False:
#        yield 1
#        
#def generator1():
#    if True:
#        yield 1 
#
#def generator2():
#    if False:   
#        yield 1
#
#g1 = generator1()
#g2 = generator2()
#
#print(type(g1))
#print(type(g2))
#print(g1.__next__())
#print(g2.__next__())