import tkinter as tk
import time
win1 = tk.Tk()
win1.title('Layout Management')
win1.geometry('300x300')
def Loginn():
	name1 = name_entry.get()
	passwd = password_entry.get()
	if passwd == f'{name1.lower()}':
		print('*****logging-in*******\n')
		time.sleep(3)
		print("-"*10+ f"{name1.upper()}You are logged in!!" + "-"*10)
	else:
		print('Wrong passwd...!!')

name_label=tk.Label(win1, text="Username: ")
name_label.grid(row=0, column=0)
name_entry =tk.Entry(win1)
name_entry.grid(row=0, column=1)

tk.Label(win1, text="Password: ").grid(row=1, column=0)
password_entry= tk.Entry(win1, show="*")
password_entry.grid(row=1, column=1)
tk.Button(win1, text="Login", command=Loginn).grid(row=2,column=1)

win1.mainloop()


'''
tkinter provides 3 main geometry managers to organize widgets;
pack() - simple, stacks widgets vertically/ horizontally
grid() - positions widgets in a table-like grid
place() - absolute positioning (rarely used)
'''
