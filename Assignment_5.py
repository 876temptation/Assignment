# Program Name: Assignment5.py
# Course: IT3883 / Section W01
# Student Name: Adrian Anderson
# Assignment Number: Assignment 5
# Due Date: 07/17/2026
# Purpose: This program reads temperature data from an input file, stores the
#          information in a SQLite database, and computes the average
#          temperature for Sunday and Thursday.
# Resources Used: Pycharm, class notes, geeksforgeeks.com

import sqlite3

# Ask user for the input filename
filename = input("Enter the temperature input filename: ")

# Create (or connect to) the SQLite database
conn = sqlite3.connect("Temperature.db")
cursor = conn.cursor()

# Create the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Temperature_Readings (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT,
        Temperature_Value REAL
    )
""")

# Read the input file and insert data into the database
with open(filename, "r") as file:
    for line in file:
        parts = line.split()
        day = parts[0]
        temp = float(parts[1])

        cursor.execute("""
            INSERT INTO Temperature_Readings (Day_Of_Week, Temperature_Value)
            VALUES (?, ?)
        """, (day, temp))

conn.commit()

# Compute average temperature for Sunday
cursor.execute("""
    SELECT AVG(Temperature_Value)
    FROM Temperature_Readings
    WHERE Day_Of_Week = 'Sunday'
""")
sunday_avg = cursor.fetchone()[0]

# Compute average temperature for Thursday
cursor.execute("""
    SELECT AVG(Temperature_Value)
    FROM Temperature_Readings
    WHERE Day_Of_Week = 'Thursday'
""")
thursday_avg = cursor.fetchone()[0]

# Print the results
print("\nAVERAGE TEMPERATURES\n")
print(f"Sunday Average: {sunday_avg:.2f}")
print(f"Thursday Average: {thursday_avg:.2f}")

# Close the database connection
conn.close()
