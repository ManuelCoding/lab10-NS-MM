# https://github.com/ManuelCoding/lab10-NS-MM
# Partner 1: Neville Shaw
# Partner 2: Manuel Martinez

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.

import math
def add(a, b): a + b

def sub(a, b): a - b

def mul(a, b): a * b

def div(a, b): b / a # raise ZeroDivisionError if a == 0

def log(a, b): loga(b)# use math library + raise ValueError

def exp(a, b): ab

"""

import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a) # raise ValueError if a < 0
def hypotenuse(a, b):
    math.hypot(a, b) # can have negative nums

# First example
def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0: raise ZeroDivisionError
    return b / a # raise ZeroDivisionError if a == 0
def logarithm(a, b):
    if b < 0: raise ValueError()
    return math.log(b, a) # use math library + raise ValueError
def exp(a, b):
    return a**b



