import socket
import threading
import time

def handle_client(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()

def main():
    s = socket.socket()
    s.bind(('localhost', 9090))
    s.listen()
    print("Threaded server running on port 9090")

    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()

if __name__ == "__main__":
    main()

