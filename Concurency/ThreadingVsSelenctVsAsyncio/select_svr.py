import socket
import select

server = socket.socket()
server.bind(('localhost', 9091))
server.listen()
server.setblocking(False)

sockets = [server]
print("Select server running on port 9091")

while True:
    readable, _, _ = select.select(sockets, [], [])
    for s in readable:
        if s is server:
            conn, addr = server.accept()
            conn.setblocking(False)
            sockets.append(conn)
        else:
            data = s.recv(1024)
            if data:
                s.sendall(data)
            else:
                s.close()
                sockets.remove(s)

