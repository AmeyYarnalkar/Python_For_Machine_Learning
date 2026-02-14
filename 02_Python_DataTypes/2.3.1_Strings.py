# Try Executing this code first then refer the notes

# =========================================================
# PRINTING OUTPUT
# =========================================================

# To print anything to the console we use print()
print("Hello World")


# =========================================================
# STRING CREATION
# =========================================================

# Creating a string with content
str1 = "test string"

# Creating an empty string
str2 = ""

print(str1)
print(str2)


# =========================================================
# CHECKING TYPE
# =========================================================

# type() tells us the data type of a value
print(type(str1))   # <class 'str'>


# =========================================================
# CONVERTING VALUES INTO STRING
# =========================================================

# str() converts any value into its string representation
print(str(0.300003))
print(str(-2.3))
print(str(True))


# =========================================================
# LENGTH OF STRING
# =========================================================

# len() gives number of characters
print(len(str1))


# =========================================================
# ACCESSING CHARACTERS (INDEXING)
# =========================================================

# Python uses 0-based indexing
print(str1[1])                 # second character
print(str1[len(str1) - 1])     # last character

# print(str2[len(str2) - 1])   # IndexError because empty string


# =========================================================
# STRING COMPARISON (UNICODE BASED)
# =========================================================

# Unicode order roughly:
# numbers < uppercase < lowercase

print("apple" > "ball")  # False because 'a' < 'b'
print("A" < "a")         # True


# =========================================================
# MEMBERSHIP CHECKING
# =========================================================

# Check if substring exists
print("a" in "apple")      # True
print("z" not in "apple")  # True


# =========================================================
# IMPORTANT OPERATIONS
# =========================================================

# -------------------------
# SLICING
# -------------------------
# s[start:end]  (end not included)

print(str1[0:2])
print(str1[:4])
print(str1[5:])


# -------------------------
# CONCATENATION
# -------------------------

# this will cause TypeError because int cannot join string
# print("str" + 12)

# ✔ Convert to string first
print("str" + str(12))

# joining two strings
print("str" + "a")


# ------------------t-------
# CHANGING CASE
# -------------------------

s = "test"

# IMPORTANT: strings are immutable
# these return NEW strings, they don't modify original

print(s.upper())       # TEST
print(s.lower())       # test
print(s.title())       # Test
print(s.capitalize())  # Test

# original remains unchanged
print(s)


# -------------------------
# REMOVING EXTRA SPACES
# -------------------------

s = "   test"
p = "test   "
q = "  test  "

print(s.lstrip())   # remove left spaces
print(p.rstrip())   # remove right spaces
print(q.strip())    # remove both sides


# -------------------------
# FINDING SUBSTRING
# -------------------------

text = "pattern test"

print(text.find("pat"))    # returns index or -1 if not found

# text.index("xyz")        # raises error if not found
# Difference:
# find()  → safe (returns -1)
# index() → strict (throws exception)


# =========================================================
# STRING TO LIST / LIST TO STRING
# =========================================================

# NOTE:
# Strings behave like list of characters:
# "str" -> ["s","t","r"]

# SPLITTING INTO LIST
data = "a,b,c"
print(data.split(","))   # ['a','b','c']


# JOINING LIST INTO STRING
chars = ["s", "t", "r"]

# delimiter.join(list)
print("".join(chars))      # "str"
print("-".join(chars))     # "s-t-r"
