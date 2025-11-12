import socket
s = socket.socket()
s.setblocking(False)
try:
	s.connect((socket.gethostname, 80))
except (socket.error, socket.timeout) as e:
	#handle the exception by checking if its connection error
	print(f'Failed to connect: {e}')
except BlockingIOError:
	pass# connection in progress, continue with other tasks
try:
	s.send(b'Hello, world')
#send data (non-blocking operation)
except: 
	BlockingIOError:
#Receive data (non-blocking operation)
try: 
	data = s.recv(1024)
except BlockingIOError:
 	pass #no data available continue with other tasks
 #close the socket
 finally:
	 s.close()