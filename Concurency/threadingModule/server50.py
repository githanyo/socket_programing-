#!/bin/python3
#socket----> bind()-----> listen() ----> accept() -----> start communication(receive and send messages)
import socket
import threading

#create the socket
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to ip and port number
server_socket.bind(('localhost', 7172))










#handle-clients
def handle_clients(conn, addr):
	while True:
		#receiving the message
		message = conn.recv(1024)
		if not message:
			print(f'client@ {addr} left!!...')
			break
		print(message.decode())
		#send reply
		reply = input('server_reply: ')
		conn.send(reply.encode())
		#close the connection 
		#conn.close()
		#server_socket.close()


#start the server and thread the clients
def start_server():
	#listen for incoming requests
	server_socket.listen(5) #allow 5 pending connections
	print('_'*50 + '\n'+'server listening on port number 7172.....\n'+'_'*50)
	while True:
		#accept connection requests
		conn, addr = server_socket.accept() #conn>>>>> (127.0.0.1(ipv4, tcp), 7171), SYN - SYN-ACK - ACK
		print(f'client@ {addr} joined the session...!!')
		thread = threading.Thread(target = handle_clients, args = (conn, addr))
		thread.start()
		online = threading.active_count()-1
		print(f'{online} members are online')

if __name__ == '__main__':
	print('~+'*25 + '\n' + '-->-->-->--->---server starting....!!!************' + '\n' + '~+')
	start_server()




"""
start searver		main thread (handle-clients)
				|
				|---> client1(handle-clients)
				|---> client2(handle-clients)
				|---> client3(handle-clients)
				|
				|(handle-clients)
"""




