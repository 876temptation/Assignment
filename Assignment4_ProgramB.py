# Program Name: Assignment4_ProgramB.py
# Course: IT3883/Section W01
# Student Name: Adrian Anderson
# Assignment Number: Assignment 4
# Due Date: 07/10/2026
# Purpose: This program listens for incoming text from Program A,
#          converts the text to uppercase, prints it locally,
#          and sends the uppercase version back to Program A.
# Resources: Pycharm, class notes, geeksforgeeks.com

import socket

# Create a TCP/IP socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hard‑coded IP and port
HOST = "127.0.0.1"
PORT = 45000

try:
    # Bind the server to the IP and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen(1)
    print("Program B is listening for a connection...")

    # Accept a connection from Program A
    conn, address = server_socket.accept()
    print("Connected to Program A at:", address)

    # Receive the string sent by Program A
    data = conn.recv(1024).decode()

    # Convert to uppercase
    upper_text = data.upper()

    # Print uppercase version in Program B
    print("Uppercase string in Program B:", upper_text)

    # Send uppercase string back to Program A
    conn.sendall(upper_text.encode())

except Exception as e:
    print("Error:", e)

finally:
    # Close the connection and socket
    conn.close()
    server_socket.close()
