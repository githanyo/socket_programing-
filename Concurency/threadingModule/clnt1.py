#!/bin/python3
import socket

HOST = 'localhost'
PORT = 8383
print("Type \"exit\" any time to disconnect!!")

def start_client():
	try:
	    	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    	client.connect((HOST, PORT))
	    	while True:
		    	print(f"Connected to server[{HOST}:{PORT}]")
		    	message = input("Enter message: ")
		    	if message.lower()== 'exit':
		    		print('You have disconnected...!!')
		    	else:
		    		client.send(message.encode())
			#receive data
		    	data = client.recv(1024)
		    	if not data:
		    		print('server disconnected...!!')
		    		break
		    	else:
		    		print(f"Server response>>>> {data.decode()}")
	except KeyboardInterrupt:
		print("you have manually ended the session!!")
	finally:
		client.close()
		print("connection ended..!!")

# Run client only when executed directly
if __name__ == "__main__":
    start_client()
