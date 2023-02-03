import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect(('127.0.0.1', 5000))

# Receive no more than 1024 bytes
message = s.recv(1024)
print(message.decode())