# ============================================
# PYTHON LISTS 
# ============================================


# --------------------------------------------
# 1) WHAT IS A LIST / HOW TO CREATE A LIST
# --------------------------------------------

# Creating a list with values
numbers = [10, 20, 30]
print("Initial list:", numbers)

# Creating an empty list
empty_list = []
print("Empty list:", empty_list)

# Creating a list using list() function
letters = list("abc")
print("List from string:", letters)



# --------------------------------------------
# 2) ACCESSING ELEMENTS FROM LIST
# --------------------------------------------

nums = [10, 20, 30, 40]

# Access first element (index starts from 0)
print("First element:", nums[0])

# Access second element
print("Second element:", nums[1])

# Access last element using negative index
print("Last element:", nums[-1])



# --------------------------------------------
# 3) ADDING ELEMENTS TO LIST
# --------------------------------------------

nums.append(50)          # adds at end
print("After append:", nums)

nums.insert(1, 15)       # insert at index 1
print("After insert:", nums)

nums.extend([60, 70])    # add multiple elements
print("After extend:", nums)



# --------------------------------------------
# 4) UPDATING ELEMENTS
# --------------------------------------------

# Change value at index 0
nums[0] = 100
print("After update:", nums)



# --------------------------------------------
# 5) CHECKING PRESENCE OF ELEMENT
# --------------------------------------------

# Using 'in' keyword to check existence
if 30 in nums:
    print("30 is present in list")

if 999 not in nums:
    print("999 is NOT present in list")



# --------------------------------------------
# 6) DELETING ELEMENTS
# --------------------------------------------

# Remove by value (removes first match)
nums.remove(15)
print("After remove:", nums)

# Remove last element
nums.pop()
print("After pop():", nums)

# Remove element at specific index
nums.pop(1)
print("After pop(1):", nums)

# Delete using del keyword
del nums[0]
print("After del:", nums)



# --------------------------------------------
# 7) ITERATING OVER LIST (LOOPING)
# --------------------------------------------

marks = [80, 90, 75]

# BEST beginner-friendly way
for item in marks:
    print("Value:", item)

# When you also want index
for index, value in enumerate(marks):
    print("Index:", index, "Value:", value)

# Less recommended beginner approach
for i in range(len(marks)):
    print("Using index:", marks[i])



# --------------------------------------------
# 8) COPYING A LIST (VERY IMPORTANT)
# --------------------------------------------

a = [1, 2, 3]

# Wrong way - both variables refer to SAME list
b = a

# Correct way - create a real copy
c = a.copy()

print("Original a:", a)
print("Reference copy b:", b)
print("Real copy c:", c)



# --------------------------------------------
# 9) NESTED LIST (LIST INSIDE LIST)
# --------------------------------------------

matrix = [[1, 2], [3, 4]]

# Access inner element
print("matrix[0][1] =", matrix[0][1])



# --------------------------------------------
# 10) CLEAR ENTIRE LIST
# --------------------------------------------

temp = [5, 6, 7]
temp.clear()
print("After clear:", temp)

# ==============================
# PYTHON LIST SLICING 
# ==============================

# Create a sample list
nums = [10, 20, 30, 40, 50]

# --------------------------------
# 1) Basic slicing (start:end)
# --------------------------------
# Start at index 1, stop before index 4
slice1 = nums[1:4]
print("nums[1:4] =", slice1)      # [20, 30, 40]


# --------------------------------
# 2) Slice from beginning
# --------------------------------
# If start is missing, Python assumes start = 0
slice2 = nums[:3]
print("nums[:3] =", slice2)       # [10, 20, 30]


# --------------------------------
# 3) Slice till the end
# --------------------------------
# If end is missing, Python goes till last element
slice3 = nums[2:]
print("nums[2:] =", slice3)       # [30, 40, 50]


# --------------------------------
# 4) Copy entire list using slicing
# --------------------------------
# nums[:] creates a NEW copy of list
copy_list = nums[:]
print("nums[:] =", copy_list)     # [10, 20, 30, 40, 50]


# --------------------------------
# 5) Using step (start:end:step)
# --------------------------------
# Step = 2 means jump every 2 positions
slice4 = nums[0:5:2]
print("nums[0:5:2] =", slice4)   # [10, 30, 50]


# --------------------------------
# 6) Reverse a list using slicing
# --------------------------------
# Step = -1 means move backwards
reverse_list = nums[::-1]
print("nums[::-1] =", reverse_list)  # [50, 40, 30, 20, 10]


# --------------------------------
# 7) Negative indexing in slicing
# --------------------------------
# -4 means 4th element from end
slice5 = nums[-4:-1]
print("nums[-4:-1] =", slice5)   # [20, 30, 40]


# --------------------------------
# IMPORTANT NOTE
# --------------------------------
# Slicing DOES NOT modify the original list
print("Original nums =", nums)   # [10, 20, 30, 40, 50]
