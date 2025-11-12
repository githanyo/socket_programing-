import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8686
ADDR = (HOST, PORT)

#Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

#data structure
client = [] #stores client socket objects 
usernames = [] #stores usernames corresponding to clients

#Broadcast function
def broadcast(message, sender_socket=None):
	for client in clients:
		if client != sender_socket: #don't send back to the sender
			try:
				client.send(message)
			except:
				#handles disconnected clients
				client.close()
				if client in clients:
					clients.remove(client)

#client Handler function
	def handle_client(client):
		while True:
			try:
				message = client.recv(1024) #receive upto 1024 bytes 
				if not message:
					break
				broadcast(message, client) #send to all other clients 
			except:
				#client disconnected - cleanup
				index = clients.index(client)
				clients.remove(client)
				username = usernames[index]
				broadcast(f'{username} left the chat!'.encode('utf-8'))
				usernames.remove(username)
				break

#Connection acceptor
def receive_connection():
	while True:
		client, address = server.accept() #wait for new connections
		print(f'Connected with {str(address)}')
		#request username from new client
		client.send("USERNAME".encode(utf-8))
		username = client.recv(1024).decode('utf-8')
		#store client info
		usernames.append(username)
		clients.append(client)
		
		print(f'Username of the client is {username}')
		broadcast(f"{username} joined the chat!".encode('utf-8'))
		client.send('Connected to the server!'.encode('utf-8'))
		
		#start thread for this client
		thread = threading.Thread(target=handle_client, args=(client,))
		thread.start()
		
		
