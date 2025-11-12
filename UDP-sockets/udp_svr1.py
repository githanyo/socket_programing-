#!/bin/python3
import socket
server= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 9090))

print('Server listening on port 9090...!!')

while True:
	datagram, addr = server.recvfrom(1024)
	print(f'Received: {datagram.decode()} from {addr}')
	reply= input('UDP_server: ')
	server.sendto(reply.encode(), addr)