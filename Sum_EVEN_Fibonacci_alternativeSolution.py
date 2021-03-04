# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:25:56 2018

@author: spardaev
"""

def sumeven(target):
    fib1 = 1
    fib2 = 1
    fib_current = 0
    sumeven = 0
    while fib_current < target:
            fib_current = fib1 + fib2
            if fib_current %2 == 0:
                sumeven = sumeven +fib_current
            fib1 = fib2
            fib2 = fib_current
    print(sumeven)