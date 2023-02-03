
# Credits :- https://www.youtube.com/watch?v=iVZj9a4fog8&list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1&index=7

# Sockets are the endpoints of a two-way communication link between two programs running on the network. Sockets may communicate within a process, between processes on the same machine, or between processes on different continents.
# Sockets may communicate via a number of different underlying transport protocols such as TCP, UDP, or SPP.
# Sockets are the means by which programs on one machine can exchange data with programs on another machine.

import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service.
port = 5000

# Bind to the port
s.bind(('127.0.0.1', port))

# Now wait for client connection.
s.listen(5)

while True:
    # Establish connection with client.
    client, addr = s.accept()
    print('Got connection from', addr)
    client.send('Thank you for connecting'.encode())
    client.close()  # Close the connection
