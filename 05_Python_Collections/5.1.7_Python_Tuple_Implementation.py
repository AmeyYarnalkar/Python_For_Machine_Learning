# ======================================
# PYTHON TUPLE - BEGINNER EXAMPLES
# ======================================

# Creating tuple
nums = (10, 20, 30)
print("Tuple:", nums)

# Access elements
print("First element:", nums[0])
print("Last element:", nums[-1])

# Single element tuple (comma required)
single = (5,)
print("Single tuple:", single)

# Iterating tuple
for item in nums:
    print("Value:", item)

# Iterating with index
for i, value in enumerate(nums):
    print("Index:", i, "Value:", value)

# Tuple containing list (inner list can change)
mixed = (1, [2,3])
mixed[1].append(4)
print("Tuple with inner list:", mixed)
