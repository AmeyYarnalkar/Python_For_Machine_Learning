"""
PHASE 2 – SAFE FILE HANDLING DEMO
Run this file step by step and observe behavior.
"""


# -----------------------------------------
# 1. Safe Iteration (Memory Efficient)
# -----------------------------------------

def safe_iteration_demo():
    print("\n--- Safe Iteration Demo ---")

    with open("demo.txt", "w", encoding="utf-8") as f:
        for i in range(5):
            f.write(f"Line {i}\n")

    with open("demo.txt", "r", encoding="utf-8") as f:
        for line in f:  # Lazy reading
            print("Read:", line.strip())


# -----------------------------------------
# 2. read() vs readlines()
# -----------------------------------------

def read_vs_readlines_demo():
    print("\n--- read() vs readlines() ---")

    with open("demo.txt", "r", encoding="utf-8") as f:
        data = f.read()
        print("Using read():")
        print(data)

    with open("demo.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        print("Using readlines():")
        print(lines)


# -----------------------------------------
# 3. Cursor + seek + tell
# -----------------------------------------

def cursor_demo():
    print("\n--- Cursor Demo ---")

    with open("demo.txt", "r", encoding="utf-8") as f:
        print("Initial position:", f.tell())

        chunk = f.read(5)
        print("Read 5 chars:", chunk)
        print("Position after read:", f.tell())

        f.seek(0)
        print("Position after seek(0):", f.tell())


# -----------------------------------------
# 4. Binary Mode Demo
# -----------------------------------------

def binary_demo():
    print("\n--- Binary Mode Demo ---")

    with open("demo.txt", "rb") as f:
        data = f.read(10)
        print("Binary data:", data)
        print("Type:", type(data))


# -----------------------------------------
# 5. Encoding Error Demo
# -----------------------------------------

def encoding_error_demo():
    print("\n--- Encoding Error Demo ---")

    # Write bytes manually (invalid utf-8 sequence)
    with open("binary_data.bin", "wb") as f:
        f.write(b'\xff\xfe\xfa')

    try:
        with open("binary_data.bin", "r", encoding="utf-8") as f:
            f.read()
    except UnicodeDecodeError as e:
        print("Caught UnicodeDecodeError:", e)


# -----------------------------------------
# 6. Write Buffer + Flush Demo
# -----------------------------------------

def flush_demo():
    print("\n--- Flush Demo ---")

    with open("flush_demo.txt", "w", encoding="utf-8") as f:
        f.write("Hello")
        f.flush()
        print("Data flushed manually.")


# -----------------------------------------
# 7. Exception Safety Demo
# -----------------------------------------

def exception_safety_demo():
    print("\n--- Exception Safety Demo ---")

    try:
        with open("demo.txt", "r", encoding="utf-8") as f:
            print("File opened safely.")
            1 / 0  # Simulated crash
    except ZeroDivisionError:
        print("Exception occurred but file closed safely.")


# -----------------------------------------
# RUN ALL DEMOS
# -----------------------------------------

if __name__ == "__main__":
    safe_iteration_demo()
    read_vs_readlines_demo()
    cursor_demo()
    binary_demo()
    encoding_error_demo()
    flush_demo()
    exception_safety_demo()

    print("\nAll Phase 2 demos completed.")