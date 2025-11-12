#!/bin/python3
import socket, select

server = socket.socket()
server.bind(('localhost', 8080))
server.listen()
server.setblocking(False)

sockets = [server]
while True:
    readable, _, _ = select.select(sockets, [], [])
    for s in readable:
        if s is server:
            conn, addr = server.accept()
            conn.setblocking(False)
            sockets.append(conn)
            print(f"New connection: {addr}")
        else:
            data = s.recv(1024)
            if data:
                s.sendall(data)
            else:
                s.close()
                sockets.remove(s)

