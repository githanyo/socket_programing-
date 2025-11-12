import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# ---------- CLIENT LOGIC ----------

def connect_to_server():
    """Connect to the socket server"""
    global client
    try:
        server_ip = ip_entry.get()
        server_port = int(port_entry.get())
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_ip, server_port))
        chat_box.insert(tk.END, f"Connected to {server_ip}:{server_port}\n")
        connect_button.config(state=tk.DISABLED)
        threading.Thread(target=receive_messages, daemon=True).start()
    except Exception as e:
        messagebox.showerror("Connection Error", f"Could not connect: {e}")

def receive_messages():
    """Receive messages from server"""
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg:
                chat_box.insert(tk.END, f"Server: {msg}\n")
                chat_box.see(tk.END)
        except:
            chat_box.insert(tk.END, "❌ Disconnected from server.\n")
            break

def send_message():
    """Send user message to server"""
    msg = msg_entry.get()
    if msg.strip() == "":
        return
    try:
        client.send(msg.encode('utf-8'))
        chat_box.insert(tk.END, f"You: {msg}\n")
        chat_box.see(tk.END)
        msg_entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Cannot send message. Not connected to server.")

# ---------- GUI SETUP ----------

root = tk.Tk()
root.title("Socket Chat Client")
root.geometry("400x500")
root.resizable(False, False)

# Server connection frame
frame_conn = tk.Frame(root)
frame_conn.pack(pady=5)

tk.Label(frame_conn, text="Server IP:").grid(row=0, column=0, padx=5)
ip_entry = tk.Entry(frame_conn, width=15)
ip_entry.grid(row=0, column=1)
ip_entry.insert(0, "127.0.0.1")

tk.Label(frame_conn, text="Port:").grid(row=0, column=2, padx=5)
port_entry = tk.Entry(frame_conn, width=5)
port_entry.grid(row=0, column=3)
port_entry.insert(0, "7171")

connect_button = tk.Button(frame_conn, text="Connect", command=connect_to_server)
connect_button.grid(row=0, column=4, padx=5)

# Chat box
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state=tk.NORMAL)
chat_box.pack(padx=10, pady=10)
chat_box.insert(tk.END, "Welcome to the Chat Client!\n")

# Message entry
frame_msg = tk.Frame(root)
frame_msg.pack(pady=5)

msg_entry = tk.Entry(frame_msg, width=30)
msg_entry.grid(row=0, column=0, padx=5)

send_button = tk.Button(frame_msg, text="Send", command=send_message)
send_button.grid(row=0, column=1)

root.mainloop()

