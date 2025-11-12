#!/bin/python3
import socket

HOST = 'localhost'
PORT = 8383
ADDR = (HOST, PORT)
#client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print("Type \"exit\" any time to exit session....!!" + "\n" +"-")
try:
	while True:
		message = input('You>>>>: ')
		if message.lower()== 'exit':
			print('You have ended the session...!!')
			break
		client.send(message.encode())
		response = client.recv(1024).decode()
		if response.lower() == "remove":
			print("server has removed you")
			break
		print(f'Server>> {response}\n')

except KeyboardInterrupt:
	print('you have manually ended the session!!!'+'\n'+'-'*50)
finally:
	print('_'*18 + 'session ended!!'+'_'*18)
	client.close()