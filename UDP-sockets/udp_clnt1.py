#!/bin/python3
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 9090)
while True:
	message = input('client: ').encode()
	client.sendto(message, server_address)
	reply, addr = client.recvfrom(1024)
	print(reply.decode())
