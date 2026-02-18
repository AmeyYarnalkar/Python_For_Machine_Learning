"""
DECORATORS REFERENCE FILE
Keep this file. Revisit anytime.
"""

from functools import wraps
import time


# ==========================================================
#  BASIC DECORATOR
# ==========================================================

def simple_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@simple_decorator
def greet():
    print("Hello")


# ==========================================================
#  DECORATOR WITH ARGUMENTS SUPPORT (*args, **kwargs)
# ==========================================================

def flexible_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function is running...")
        result = func(*args, **kwargs)
        print("Function finished.")
        return result
    return wrapper


@flexible_decorator
def add(a, b):
    return a + b


# ==========================================================
#  DECORATOR WITH ITS OWN ARGUMENTS
# ==========================================================

def repeat(n):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return actual_decorator


@repeat(3)
def say_hi():
    print("Hi")


# ==========================================================
#  TIMING DECORATOR (REAL-WORLD USE)
# ==========================================================

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1)


# ==========================================================
#  STACKING DECORATORS
# ==========================================================

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


def add_exclamation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"
    return wrapper


@add_exclamation
@uppercase
def welcome():
    return "welcome"


# ==========================================================
# PROPERTY (SPECIAL DECORATOR)
# ==========================================================

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


# ==========================================================
# RUN SECTION (Optional Testing) -> We will learn about this in the next module
# ==========================================================

if __name__ == "__main__":
    greet()

    print(add(2, 3))
    
    say_hi()

    slow_function()

    print(welcome())

    p = Person(25)
    print(p.age)
    p.age = 30
    print(p.age)
