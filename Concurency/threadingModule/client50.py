import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 7172))

try:
	while True:
		message = input('client: ')
		if message.lower()=='exit':
			print('You have ended the session')
			break
		else:
			client.send(message.encode())
		#receive reply
		response = client.recv(1024).decode().strip()
		if response.lower()== 'disconnect':
			print("Server bounced You, go home!!!....")
			break
		else:
			print(response)
except KeyboardInterrupt:
	print('You have manually ended the session!!....')
finally:
	print('Connection closed')
	client.close()
