#!/bin/python3
import tkinter as tk
from tkinter import scrolledtext, messagebox

root = tk.Tk()
root.title("Socket Chat Client")
root.geometry("400x500")
root.resizable(False, False)

def connect_to_server():
	pass
def send_message():
	pass


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
port_entry.insert(0, "8080")

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
