# Program Name: Assignment4_ProgramA.py
# Course: IT3883/Section W01
# Student Name: Adrian Anderson
# Assignment Number: Assignment 4
# Due Date: 07/10/2026
# Purpose: This program prompts the user for a string, sends it to Program B
#          over a TCP socket, waits for a response, and prints the result.
# Resources: Pycharm,class notes, geeksforgeeks.com

import socket

# Create a TCP/IP socket object

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hard‑coded IP and port (Program B must use the same)
SERVER_IP = "127.0.0.1"
SERVER_PORT = 45000

try:
    # Connect to Program B (server)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    # Prompt user for input and send it to Program B
    user_text = input("Enter a string to send to Program B: ")
    client_socket.sendall(user_text.encode())

    # Wait for the uppercase response from Program B
    response = client_socket.recv(1024).decode()
    print("Received from Program B:", response)

except Exception as e:
    print("Error:", e)

finally:
    client_socket.close()
