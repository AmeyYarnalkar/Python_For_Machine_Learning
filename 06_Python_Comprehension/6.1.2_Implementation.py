# ====================================
# PYTHON COMPREHENSIONS - EXAMPLES
# ====================================

# Simple list comprehension
nums = [x for x in range(5)]
print("List:", nums)

# List comprehension with if
evens = [x for x in range(10) if x % 2 == 0]
print("Evens:", evens)

# List comprehension with if-else
labels = ["even" if x%2==0 else "odd" for x in range(5)]
print("Labels:", labels)

# Tuple (using generator + tuple())
t = tuple(x for x in range(5))
print("Tuple:", t)

# Set comprehension
s = {x*x for x in range(5)}
print("Set:", s)

# Dict comprehension
d = {x: x*x for x in range(5)}
print("Dict:", d)
