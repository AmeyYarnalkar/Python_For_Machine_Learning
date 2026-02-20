"""
PHASE 3 CSV, JSON, PICKLE DEMO
Simple, clean, runnable examples
"""

import csv
import json
import pickle


# -----------------------------------------
#  CSV DEMO
# -----------------------------------------

def csv_demo():
    print("\n--- CSV DEMO ---")

    # Writing CSV
    with open("students.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "score"])
        writer.writerow(["Amey", 22, 90])
        writer.writerow(["Rohit", 21, 85])

    # Reading CSV
    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print("Row:", row, "| Types:", [type(x) for x in row])


# -----------------------------------------
#  JSON DEMO
# -----------------------------------------

def json_demo():
    print("\n--- JSON DEMO ---")

    data = {
        "name": "Amey",
        "age": 22,
        "skills": ["Python", "ML"],
        "active": True
    }

    # Writing JSON
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    # Reading JSON
    with open("data.json", "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("Loaded JSON:", loaded)
    print("Type of age:", type(loaded["age"]))
    print("Type of active:", type(loaded["active"]))


# -----------------------------------------
# PICKLE DEMO
# -----------------------------------------

def pickle_demo():
    print("\n--- PICKLE DEMO ---")

    data = {
        "name": "Amey",
        "scores": [90, 85, 88],
        "meta": ("experiment1", 2026)
    }

    # Writing Pickle (binary)
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)

    # Reading Pickle (binary)
    with open("data.pkl", "rb") as f:
        loaded = pickle.load(f)

    print("Loaded Pickle:", loaded)
    print("Type of meta:", type(loaded["meta"]))


# -----------------------------------------
# RUN ALL
# -----------------------------------------

if __name__ == "__main__":
    csv_demo()
    json_demo()
    pickle_demo()

    print("\nPhase 3 demo completed.")