# Program Name: Final Exam - Sprint 2 Implementation
# Course: IT3883/Section W01
# Student Name: Adrian Anderson
# Assignment Number: Final Exam
# Due Date: 07/26/2026
# Purpose: # This program reads sentences describing quantities of coins
           # and converts them into a total dollar amount.
# Resources: Pycharm,class notes, geeksforgeeks.com

# Dictionary mapping coin names to their dollar values
VALUES = {
    "penny": 0.01,
    "pennies": 0.01,
    "nickel": 0.05,
    "nickels": 0.05,
    "dime": 0.10,
    "dimes": 0.10,
    "quarter": 0.25,
    "quarters": 0.25
}

def conversion(sentence):
    # Split the sentence into groups separated by "and"
    groups = sentence.split(" and ")
    total = 0.0

    for group in groups:
        words = group.split()
        quantity = int(words[0])          # First word is the number
        denomination = words[1].lower()   # Second word is the coin type

        # Multiply quantity by coin value from dictionary
        total += quantity * VALUES[denomination]

    # Return formatted dollar amount
    return f"{total:.2f}"

# Print Header and Instructions Once
print("*****Coin Converter Program*****")
print("Type 'quit' to exit.\n")
print("Enter a sentence to convert:")

while True:
    user_input = input()

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    try:
        result = conversion(user_input)
        print("\n", user_input,"->", result)
    except Exception as e:
        print("\nInvalid input.\n")