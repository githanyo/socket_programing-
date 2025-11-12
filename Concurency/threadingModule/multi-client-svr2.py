#!/bin/python3
import socket
import threading

HOST = 'localhost'
PORT = 8181
ADDR = ('localhost', PORT)

#FUNCTION TO HANDLE EACH CLIENT CONNECTION
def handle_client(conn, addr):
	print(f'Client: {addr} connected')
	while True:
		message = conn.recv(1024)
		if not message:
			print('A member disconnected...!!')
			break
		print(f"client[{addr}] >>> {message.decode()}")
		response = input(f'Server-Response @client{addr}>>> ').encode()
		conn.sendall(response)
def start_server():
	#server continueously listen allow 5 pending connections
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(ADDR)
	server.listen(5)
	print(f"Server is listening on {HOST}:{PORT}.....!!")
	#thread clients
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target = handle_client, args = (conn, addr))
		thread.start()
		online = threading.active_count()-1
		print(f'\nOnline-Clients-------> {online} members')


if __name__ == "__main__":
	print("Server is starting.....!!")
	start_server()