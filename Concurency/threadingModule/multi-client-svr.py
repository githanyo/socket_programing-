#!/bin/python3
import socket
import threading

HOST = 'localhost'
PORT = 8080

#FUNCTION TO HANDLE EACH CLIENT CONNECTION
def handle_client(conn, addr):
	print(f'[New Connection] {addr} connected.')
	while True:
		data = conn.recv(1024)
		if not data:
			break #client disconnected
		print(f'Received message from {addr}: {data.decode()}')
		conn.sendall(b'hello client, wassap??')
	conn.close()
	print(f'[DISCONNECTED] {addr} disconnected..!!')

#main server function 
def start_server():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((HOST, PORT))
	server.listen(5) #Allow upto 5 pending connections
	print(f'[Listening] Server is listening on{HOST}:{PORT}')
	
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args= (conn, addr))
		thread.start()
		print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')

if __name__ == "__main__":
	print("[STARTING] Server is starting")
	start_server()