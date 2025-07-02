# utils.py
import random

def spin_wheel():
    from config import WHEEL_NUMBERS
    return random.choice(WHEEL_NUMBERS)

def is_red(number):
    from config import RED_NUMBERS
    return number in RED_NUMBERS

def is_black(number):
    from config import BLACK_NUMBERS
    return number in BLACK_NUMBERS

def is_odd(number):
    if isinstance(number, int):
        return number % 2 == 1
    return False

def is_even(number):
    if isinstance(number, int):
        return number % 2 == 0
    return False

def is_high(number):
    if isinstance(number, int):
        return 19 <= number <= 36
    return False

def is_low(number):
    if isinstance(number, int):
        return 1 <= number <= 18
    return False
