# Program Name: Assignment1.py
# Course: IT3883/Section 501
# Student Name: Adrian Anderson
# Assignment Number: Lab #1
# Due Date: 06/12/2026

# Purpose: This allows the user to append text to an input buffer,clear the buffer, display the current buffer contents and exit the program.
#   The program loops displays the menu until the user chooses to exit.
#
# Resources Used:
#   1). Python documentation (input, loops, strings)
#   2). Class lecture notes
#   3).  Pycharm


# Initialize the input buffer

input_buffer = ""

# Main program loop

while True:
    # PRINT MENU WITH OPTIONS
    print("\n----- TEXT BUFFER MENU ----\n1. Append data to the input buffer\n2. Clear the input buffer\n3. Display the input buffer\n4. Exit the program")


    # ASK USER TO INPUT CHOICE
    choice = input("Enter your choice (1-4): ")

    # OPTION 1: APPEND DATA TO THE INPUT BUFFER
    if choice == "1":
        user_text = input("Enter text to append: ")
        input_buffer += user_text  # Append to existing buffer
        print("Text appended successfully.")

    # OPTION 2: CLEAR THE INPUT BUFFER
    elif choice == "2":
        input_buffer = ""  # Reset buffer
        print("Input buffer cleared.")

    # OPTION 3: DISPLAY CURRENT INPUT BUFFER
    elif choice == "3":
        print("\n--- Current Input Buffer ---")
        if input_buffer:
            print(input_buffer)
        else:
            print("Buffer is empty")

    # OPTION 4: END PROGRAM
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    # INVALID INPUT
    else:
        print("Your choice is invalid. Please enter a number between 1 and 4.")
