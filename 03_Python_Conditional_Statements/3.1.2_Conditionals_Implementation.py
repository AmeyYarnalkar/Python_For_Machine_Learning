# =========================================================
# CONDITIONAL STATEMENTS IN PYTHON
# =========================================================


# ---------------------------------------------------------
# Check if number is even or odd
# ---------------------------------------------------------

num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# ---------------------------------------------------------
# Check positive, negative, or zero
# ---------------------------------------------------------

x = -5

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")


# ---------------------------------------------------------
# Check voting eligibility
# ---------------------------------------------------------

age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


# ---------------------------------------------------------
# Find largest among two numbers
# ---------------------------------------------------------

a = 10
b = 25

if a > b:
    print("a is larger")
else:
    print("b is larger")


# ---------------------------------------------------------
# Grade checking using multiple conditions
# ---------------------------------------------------------

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# =========================================================
# MATCH-CASE EXAMPLE (Python 3.10+)
# =========================================================

day = "monday"

match day:
    case "monday":
        print("Start of week")
    case "friday":
        print("Weekend coming")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Normal day")
