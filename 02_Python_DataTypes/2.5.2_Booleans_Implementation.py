# =========================================================
# BOOLEANS IN PYTHON — SIMPLE IMPLEMENTATION
# =========================================================

# ---------------------------------------------------------
# BASIC BOOLEAN VALUES
# ---------------------------------------------------------

x = True
y = False

print(x)
print(y)
print(type(x))      # <class 'bool'>


# ---------------------------------------------------------
# BOOL IS SUBCLASS OF INT
# ---------------------------------------------------------

print(True == 1)    # True
print(False == 0)   # True

# behaves like integers
print(True + True)  # 2
print(False + 10)   # 10


# ---------------------------------------------------------
# SINGLETON BEHAVIOR
# ---------------------------------------------------------

print(True is True)
print(False is False)


# ---------------------------------------------------------
# TRUTHY AND FALSY VALUES
# ---------------------------------------------------------

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(range(0)))

print(bool("hello"))   # truthy
print(bool([1, 2]))    # truthy


# ---------------------------------------------------------
# COMPARISON OPERATORS
# ---------------------------------------------------------

print(5 > 3)
print(5 == 5)
print(3 != 2)
print(10 >= 10)

x = 5
print(1 < x < 10)   # chained comparison


# ---------------------------------------------------------
# LOGICAL OPERATORS
# ---------------------------------------------------------

print(True and True)
print(True or False)
print(not True)

# IMPORTANT:
# and/or return operands
print(5 and 10)     # 10
print(0 and 10)     # 0
print(5 or 10)      # 5
print(0 or 10)      # 10


# ---------------------------------------------------------
# SHORT CIRCUITING DEMO
# ---------------------------------------------------------

# Right side not evaluated
print(False and (10 / 0))   # No error because left is False

# Right side not evaluated
print(True or (10 / 0))     # No error because left is True


# ---------------------------------------------------------
# USING BOOLEANS IN CONDITIONS
# ---------------------------------------------------------

flag = True

if flag:
    print("Correct boolean check")


# Empty container condition
my_list = []

if my_list:
    print("List has items")
else:
    print("List is empty")


# ---------------------------------------------------------
# DEFAULT VALUE USING OR (EDGE CASE)
# ---------------------------------------------------------

user_input = 0
value = user_input or "default"
print(value)   # shows "default" because 0 is falsy


# ---------------------------------------------------------
# HOW PYTHON DECIDES TRUTHINESS
# ---------------------------------------------------------

class A:
    def __bool__(self):
        return False

obj = A()

if obj:
    print("Truthy")
else:
    print("Falsy because __bool__ returned False")


class B:
    def __len__(self):
        return 0

obj2 = B()

if obj2:
    print("Truthy")
else:
    print("Falsy because length is 0")


# ---------------------------------------------------------
# INTERNAL BEHAVIOR OF AND / OR
# ---------------------------------------------------------

a = 0
b = 100
print(a and b)   # returns a (falsy)

a = 50
print(a or b)    # returns a (truthy)
