# ===============================
# PYTHON FUNCTIONS PRACTICE FILE
# ===============================

# 1️⃣ Simple Function
def square(n):
    return n * n


# 2️⃣ Return vs Print
def add_print(a, b):
    print(a + b)


def add_return(a, b):
    return a + b


# 3️⃣ Default Parameter
def greet(name="Guest"):
    return f"Hello {name}"


# 4️⃣ *args Practice
def multiply_all(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


# 5️⃣ **kwargs Practice
def print_info(**data):
    formatted = ", ".join(f"{key.capitalize()}: {value}" for key, value in data.items())
    return formatted


# 6️⃣ Keyword-only Parameter
def calculate_total(price, *, tax):
    return price + tax


# 7️⃣ Function as Object
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


operations = [add, multiply]


# 8️⃣ Annotations
def divide(a: float, b: float) -> float:
    return a / b


# 9️⃣ Internal Inspection
def sample_function(x, y=10):
    return x + y


# 🔟 Mini Calculator Engine
def operate(a, b, operation):
    return operation(a, b)


# ===============================
# TESTING SECTION
# ===============================

if __name__ == "__main__": # 👈 Avoid this for now we will learn it in upcoming modules

    print("Square:", square(5))

    add_print(2, 3)
    result = add_return(2, 3)
    print("Returned Sum:", result)

    print(greet())
    print(greet("Amey"))

    print("Multiply All:", multiply_all(2, 3, 4))

    print(print_info(name="Amey", age=21))

    print("Total:", calculate_total(100, tax=18))

    print("Operations:")
    for op in operations:
        print(op(2, 3))

    print("Divide:", divide(10, 2))
    print("Annotations:", divide.__annotations__)

    print("Function Name:", sample_function.__name__)
    print("Defaults:", sample_function.__defaults__)
    print("Var Names:", sample_function.__code__.co_varnames)

    print("Operate Add:", operate(2, 3, add))
    print("Operate Multiply:", operate(2, 3, multiply))
