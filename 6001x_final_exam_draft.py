#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 23:06:10 2017

@author: sss
"""

#from operator import itemgetter, methodcaller

#trans = {'0':'ling', 
#         '1':'yi', 
#         '2':'er', 
#         '3':'san', 
#         '4':'si', 
#         '5':'wu', 
#         '6':'liu',
#         '7':'qi', 
#         '8':'ba', 
#         '9':'jiu',
#         '10': 'shi'}
#
#def convert_to_mandarin(us_num):
#    '''
#    us_num, a string representing a US number 0 to 99
#    returns the string mandarin representation of us_num
#    '''
#    num = int(us_num)
#    if num <= 10:
#        return trans[us_num]
#    elif num < 20:
#        return 'shi ' + trans[str(num%10)]
#    elif num % 10 == 0:
#        return trans[str(num//10)] + ' shi'
#    else:
#        return trans[str(num//10)] + ' shi ' + trans[str(num%10)]
#        
#        
#
##test
#for i in range(100):
#    print(convert_to_mandarin(str(i)))
    
    
# longest run
#max([1,2,3])


#def longest_run_draft(L):
#    '''
#    Assumes L is a list of integers containing at least 2 elements.
#    Finds the longest run of numbers in L, where the longest run can
#    either be monotonically increasing or monotonically decreasing.
#    In case of a tie for the longest run, choose the longest run 
#    that occurs first.
#    Does not modify the list.
#    Returns the sum of the longest run.
#    '''
#    
#    #longest monotonically increasing
#    sub_list = []
#    result_list = []
    
#==============================================================================
#     # 第一次尝试，L 中的最后一个 run 捕捉不到。
#     for i in range(len(L)-1):
#         if len(sub_list) == 0:
#             sub_list = [L[i]]
#         if L[i+1] < L[i]:
#             if len(sub_list) > 1:
#                 result_list.append(sub_list)
#             sub_list = []
#             continue
#         sub_list.append(L[i+1])
#     return result_list
#==============================================================================

#==============================================================================
#     # 第二次尝试，结果中有重复自列表。
#     for i in range(len(L)-1):
#         sub_list = [L[i]]
#         for j in range(i, len(L)-1):
#             if L[j+1] >= L[j]:
#                 sub_list.append(L[j+1])
#                 i = i + 1
#             else:
#                 break
#         if len(sub_list) > 1:
#             result_list.append(sub_list)
#     return result_list
#==============================================================================
    
#==============================================================================
#     # 第三次尝试，用 while 中对 i 的跳过来避免第二种方法中的重复问题。
#     # 此方法也有问题，可能跳过第一个 run。
#     i = 0
#     while i < len(L):
#         sub_list = [L[i]]
#         for j in range(i, len(L)-1):
#             if L[j+1] >= L[j]:
#                 sub_list.append(L[j+1])
#             else:
#                 break
#         if len(sub_list) > 1 and L[i] < L[i-1]:
#             result_list.append(sub_list)
#         i += 1
#     return result_list
#==============================================================================


def longest_run(L):
    '''
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    '''
    # 1. longest monotonically increasing run
    sub_incre_list = []
    all_result_incre_list = []
    i = 0
    while i < len(L):
        sub_incre_list = [L[i]]
        for j in range(i, len(L)-1):
            if L[j+1] >= L[j]:
                sub_incre_list.append(L[j+1])
            else:
                break
        if len(sub_incre_list) > 1:
            all_result_incre_list.append([i] + [sub_incre_list])
        i += 1

    # 2. longest monotonically decreasing run
    sub_decre_list = []
    all_result_decre_list = []
    i = 0
    while i < len(L):
        sub_decre_list = [L[i]]
        for j in range(i, len(L)-1):
            if L[j+1] <= L[j]:
                sub_decre_list.append(L[j+1])
            else:
                break
        if len(sub_decre_list) > 1:
            all_result_decre_list.append([i] + [sub_decre_list])
        i += 1

    # 3. result
    r = all_result_incre_list + all_result_decre_list
    r = sorted(r, key=(lambda x: (len(x[1]), -x[0])), reverse=True)
    return sum(r[0][1])

    
def test_longest_run_final(L):
    print(longest_run(L))

test_list_1 = [9, 10, 2, 4, 5, 3, 8, 3, 4, 5, 7, 7, 2, 9, 1, 2, 3, 4, 5]
test_list_2 = [1, 2, 3, 4, 5]
test_list_3 = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
test_list_4 = [5, 4, 10]

test_longest_run_final(test_list_1)
test_longest_run_final(test_list_4)
