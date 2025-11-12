import tkinter as tk
import socket
import threading

client = socket.socket()
client.connect(('localhost', 7171))

def send_message():
	msg = message_entry.get()
	client.send(msg.encode())
	message_entry.delete(0, tk.END)
	
win1 = tk.Tk()
win1.title("Isbat Chatroom")

chat_box = tk.Text(win1)
chat_box.pack()
message_entry=tk.Entry(win1)
message_entry.pack()

send_button = tk.Button(win1, text="Send", command=send_message)
send_button.pack()

win1.mainloop() 
