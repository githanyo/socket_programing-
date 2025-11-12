#!/bin/python3
import socket, threading
import tkinter as tk 
from tkinter import messagebox, scrolledtext

global client
def end_session():
	chat_box.config(state=tk.NORMAL)
	chat_box.insert(tk.END,'You have Disconnected!!')
	chat_box.config(state=tk.DISABLED)
	connect_button.config(text='Re-connect', command=connect_to_server)
	client.close()
def send_message():
	name=name_entry.get()
	msg=msg_entry.get()
	try:
		client.sendall(msg.encode())
		chat_box.config(state=tk.NORMAL)
		chat_box.insert(tk.END, f'\n{name}: {msg}')
		chat_box.see(tk.END)
		chat_box.config(state=tk.DISABLED)
		msg_entry.delete(0, tk.END)


	except Exception as e:
		messagebox.showerror('Failed to send!!', f'Error: {e}')

def receive_message():
	while True:
		try:
			reply = client.recv(1024).decode()
			if reply:
				chat_box.config(state=tk.NORMAL)
				chat_box.insert(tk.END, f'\nServer: {reply}')
				chat_box.see(tk.END)
				chat_box.config(state=tk.DISABLED)
		
		except:
			chat_box.config(state=tk.NORMAL)
			chat_box.insert(tk.END, 'Disconnected from Server!!')
			chat_box.config(state=tk.DISABLED)
			break

def connect_to_server():
	global client
	try:
		HOST=ip_entry.get()
		PORT=int(port_entry.get())
		if not HOST or not PORT:
			return
		client=socket.socket()
		conn=client.connect((HOST, PORT))
		#if conn:
		'''connect_button.config(state=tk.DISABLED)

		messagebox.showinfo('Connection esstablished successfully!!')'''
		
		chat_box.config(state=tk.NORMAL)
		chat_box.insert(tk.END, f'connected to server {HOST}:{PORT}')
		chat_box.config(state=tk.DISABLED)
		threading.Thread(target=receive_message, daemon=True).start()
		connect_button.config(text='Disconnect', command=end_session)
	except Exception as e:
		messagebox.showerror('Connection Error', f'Failed to connect!!>> {e}')



win1 = tk.Tk()
win1.title('ISBAT CHAT ROOM')
win1.geometry('500x500')
win1.resizable(False, False)

#-----LOGIN FRAME-----------------------
frame_win1 = tk.Frame(win1)
frame_win1.pack(pady=5)

tk.Label(frame_win1, text='Username: ').grid(row=0, column=0)
name_entry = tk.Entry(frame_win1, width=20)
name_entry.grid(row=0, column=1, padx=5)

# server connection
tk.Label(frame_win1, text='Server IP:').grid(row=1, column=0, padx=5)
ip_entry = tk.Entry(frame_win1, width=15)
ip_entry.grid(row=1, column=1)
ip_entry.insert(0, '127.0.0.1')

# port number
tk.Label(frame_win1, text='Port:').grid(row=1, column=2)
port_entry = tk.Entry(frame_win1, width=6)
port_entry.grid(row=1, column=3)
port_entry.insert(0, '8080')

# connect button
connect_button = tk.Button(frame_win1, text='Connect', command=connect_to_server)
connect_button.grid(row=1, column=4, padx=5)

#-----CHAT SCREEN-----------------
chat_box = scrolledtext.ScrolledText(win1, wrap=tk.WORD, width=58, height=20, state=tk.DISABLED)
chat_box.pack(padx=10, pady=10)
chat_box.config(state=tk.NORMAL)
chat_box.insert(tk.END, 'Welcome to ISBAT CHAT ROOM!!\n')
chat_box.config(state=tk.DISABLED)

#------MESSAGE BOX--------------------
msg_frame = tk.Frame(win1)
msg_frame.pack(padx=10, pady=5)

# MESSAGE ENTRY------------------
msg_entry = tk.Entry(msg_frame, width=50)
msg_entry.grid(row=0, column=0, padx=10)

# send button
send_button = tk.Button(msg_frame, text='SEND', command=send_message)
send_button.grid(row=0, column=1, padx=5)

win1.mainloop()
