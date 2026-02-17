# ==========================================
# PYTHON GENERATORS - PRACTICE FILE
# ==========================================


#  Basic Generator Function
def simple_generator():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")


print("---- Basic Generator ----")
g = simple_generator()

print(next(g))   # Predict before running
print(next(g))

try:
    print(next(g))
except StopIteration:
    print("Generator exhausted")


# ==========================================


#  Generator Expression vs List
print("\n---- Generator Expression ----")

gen_exp = (x * x for x in range(5))
print(gen_exp)  # Notice: not a list

for value in gen_exp:
    print(value)

print("Trying to reuse generator:")
for value in gen_exp:
    print(value)  # Won't print anything


# ==========================================


#  Infinite Generator
def counter():
    i = 1
    while True:
        yield i
        i += 1


print("\n---- Infinite Generator ----")
c = counter()

print(next(c))
print(next(c))
print(next(c))


# ==========================================


#  Memory Efficient File Reading Simulation
def fake_large_data():
    for i in range(1000000):
        yield f"Row {i}"


print("\n---- Simulated Large Data ----")
data_stream = fake_large_data()

for _ in range(3):
    print(next(data_stream))


# ==========================================


#  Generator vs List Memory Comparison
print("\n---- Memory Comparison ----")

list_data = [x for x in range(1000000)]
gen_data = (x for x in range(1000000))

print("List created.")
print("Generator created.")
