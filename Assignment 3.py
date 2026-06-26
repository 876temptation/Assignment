# Program Name: Assignment3.py
# Course: IT3883/Section 501
# Student Name: Adrian Anderson
# Assignment Number: Lab#3
# Due Date: 06/26/2026
# Purpose: This program creates a GUI that converts Miles per Gallon into Kilometers per Liter.
# The conversion updates live as the user types, without needing a button.

# Resources: Pycharm, Tkinter , class notes, geeksforgeeks.com

import tkinter as tk

# Assign conversion constant
converter = 0.425143707

def convert(*args):
    try:
        mpg_value = float(mpg_entry.get())   # Try converting input to float
        kml_value = mpg_value * converter   # Perform conversion
        result.set(f"{kml_value:.4f}")   # Display result rounded to 4 decimals
    except:
        result.set("")  # Clear output if input is invalid

# Create main window
window = tk.Tk()
window.title("Unit Converter")
# Label for MPG input
tk.Label(window, text="Miles per Gallon (mpg):").grid(row=0, column=0, padx=10, pady=10)

# Entry box for MPG input
mpg_entry = tk.Entry(window)
mpg_entry.grid(row=0, column=1, padx=10, pady=10)

# Variable to hold the result
result = tk.StringVar()

# Label for KM/L output
tk.Label(window, text="Kilometers per Liter (km/l):").grid(row=1, column=0, padx=10, pady=10)
tk.Label(window, textvariable=result).grid(row=1, column=1, padx=10, pady=10)

# Allows the conversion happens automatically as user types
mpg_entry.bind("<KeyRelease>", convert)

# Initiate GUI loop
window.mainloop()
