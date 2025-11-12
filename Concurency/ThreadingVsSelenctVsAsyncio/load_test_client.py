import socket
import threading
import time

SERVER_HOST = 'localhost'
SERVER_PORT = 9092   # change this to 9091 or 9092 for other servers
NUM_CLIENTS = 5000  # adjust for testing load
MESSAGE = b"ping"

def client_task():
    s = socket.socket()
    s.connect((SERVER_HOST, SERVER_PORT))
    start = time.time()
    s.sendall(MESSAGE)
    s.recv(1024)
    s.close()
    return time.time() - start

def run_test():
    start_all = time.time()
    threads = []
    for _ in range(NUM_CLIENTS):
        t = threading.Thread(target=client_task)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"Completed {NUM_CLIENTS} requests in {time.time() - start_all:.2f}s")

if __name__ == "__main__":
    run_test()

