import socket
#create a blocking socket
s = socket.socket()

#connect to a server (blocking operation)
s.connect((socket.gethostname(), 80))

#s.send(b'Hello, world')

#receive data 
data.rec