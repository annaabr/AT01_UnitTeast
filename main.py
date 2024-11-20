# ---------------------------------------------------------
# Домашнее задание
def remainder(a,b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return a % b
# ---------------------------------------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('На ноль делить нельзя')
    return a / b

def is_even(number):
    return number % 2 == 0