#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 21:58:25 2017

@author: sss
"""


"""
String slicing

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

"""
s = 'Python'
print(s[0:15])    # Python
print(s[1::2])    # yhn
print(s[-1])      # n
print(s[::-1])    # nohtyP
print(s[1:-2])    # yth



# Sum from 1 to 100
my_sum = 0
for i in range(1, 101):
    my_sum += i
print(my_sum)
# # Using reduce
import functools
my_reduce_sum = functools.reduce(lambda x, y: x+y, [i for i in range(1, 101)])
print(my_reduce_sum)



# PS1.2
# Substring counts.
s = input('Enter a string of lower case characters: ')
bob_count = 0
while True:
    if len(s) < 3:
        print('Number of times bob occurs is: 0')
        break
    for i in range(len(s)-2):
        if s[i:i+3] == 'bob':
            bob_count += 1
    print('Number of times "bob" occurs is: ' + str(bob_count))
    break



# PS1.3
# Longest substring in which letters occur in alphabetical order.
# 需要改进
s = input('Enter a string of lower case characters: ')
sub_strs = []
for i in range(len(s)):
    sub_str = s[i]
    for j in range(i, len(s)-1):
        if s[j+1] < s[j]:
            break
        sub_str += s[j+1]
    if len(sub_strs) == 0 or len(sub_str) >= len(sub_strs[-1]):
        sub_strs.append(sub_str)
if len(sub_strs) > 0:
    print('Longest substring in alphabetical order is: ',
          [s for s in sub_strs if len(s) >= len(sub_strs[-1])][0])



# Approximate solution - cube root
cube = 35
epsilon = 0.01
guess = 0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess < cube:
    guess += increment
    num_guesses += 1
    print('now guess is', guess)
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)



# E.2.3.2
x = 25
epsilon = 0.01
step = 0.001
guess = 0.0
while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
        print('guess is now', guess)
    else:
        break
if abs(guess**2-x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))



# E.2.3.3 guess my number
low = 0
high = 100
guess = 50
print('Please think of a number between 0 and 100!')
while True:
    print('Is your secret number ' + str(guess) + '?')
    s = input("Enter 'h' to indicate the guess is too high.\n"
              "Enter 'l' to indicate the guess is too low.\n"
              "Enter 'c' to indicate I guessed correctly.\n"
              "Enter now: ")
    if s == 'h':
        high = guess
    elif s == 'l':
        low = guess
    elif s == 'c':
        print('Game over. Your secret number was:', guess)
        break
    else:
        print('Sorry, I did not understand your input.')
        continue
    guess = int((low + high) / 2)



# Decimal to Binary Fraction
x = float(input('Enter a decimal(ie: 2.3): '))
p = 0
while ((2**p)*x) % 1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1
print('p is:', p)
num = int(x*(2**p))
print('num is:', num)
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
print('len(result) is:', len(result))
for i in range(p - len(result)):
    result = '0' + result
print('len(result) is now:', len(result))
print('result[0:-p] is:', result[0:-p])
if len(result[0:-p]) == 0:
    result = '0' + '.' + result[-p:]
else:
    result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal', str(x), 'is:\n' +
      str(result))



# Why use abs(a-b) < epsilon instead of a == b to determine if a equals to b?
c = 0.1
b = 0.3
a = c * 3
print('a:', a)
print('b:', b)
print('a == b? ', a == b)
print('abs(a-b) is:', abs(a-b))



# Newton-Raphson, find square root
epsilon = 0.001
y = 54.0
guess = y / 2.0
num_guesses = 0
while abs(guess*guess - y) >= epsilon:
    num_guesses += 1
    guess = guess - (guess**2 - y)/(2*guess)
print('num_guesses:', num_guesses)
print('Square root of ' + str(y) + ' is about ' + str(guess))
