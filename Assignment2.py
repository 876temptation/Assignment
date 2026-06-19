# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Adrian Anderson
# Assignment Number: Lab #1
# Due Date: 06/19/2026

# Read the input file.

# Prompt user to enter the file's name
filename = input("Enter the input file's name: ")

students = []

# Process each line in the file
with open(filename, "r") as file:
    for line in file:
        parts = line.split()              # split line into fields
        name = parts[0]                   # first field is the student's name
        scores = parts[1:]                # the other fields are the scores

        scores = [int(num) for num in scores]
        avg = sum(scores) / len(scores)
        students.append((name, avg))

# Sort in descending order by average
students.sort(key=lambda x: x[1], reverse=True)

# Print results
print("\nFinal Averages from highest to lowest:")
for name, avg in students:
    print(f"{name} {avg:.2f}")
