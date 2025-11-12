#!/bin/python3
import socket
import threading
HOST = 'localhost'
PORT = 8383
ADDR = (HOST, PORT)

#handle clients
def client_handle(conn, addr):
	message = conn.recv(1024).decode().strip()
	while True:
		if not message:
			print(f'client: {addr} disconnected...!!')
		print(f'client@{addr}--> {message}\n')
		#server response
		response = input('Server->Client{addr}: ')
		conn.sendall(response.encode())

#Start server
def start_server():
	#create server socket & listen
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(ADDR)
	server.listen(5) #allow 5 pending connections
	print(f'Server listening on {ADDR}....!!')


	#thread clients
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=client_handle, args = (conn, addr))
		thread.start()
		ONLINE = threading.active_count()-1
		print(f"Oline-clients--> {ONLINE} members")

if __name__=="__main__":
	print('~*'*25)
	print("| Server Starting....!!!" + " "*24 + "|")
	print('~*'*25)
	start_server()

