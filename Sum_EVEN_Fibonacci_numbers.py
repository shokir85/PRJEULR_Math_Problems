# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:02:29 2018

@author: spardaev
"""
def FibEvenSum(n):
    if n ==1 or n ==2:
        return 1
    fib_list = [None]*(n+1)
    fib_list[1] = 1
    fib_list[2] = 1 
    sumEven = 0
    sumOdd = 0
    total = 0
    for i in range (3, n+1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
        total = total +fib_list[i]
        if fib_list[i]%2 == 0:
            sumEven = sumEven + fib_list[i]
        else:
            sumOdd = sumOdd + fib_list[i]
        sumAll = sumEven + sumOdd
        print(sumEven, sumOdd, total, sumAll)
    return fib_list[n]