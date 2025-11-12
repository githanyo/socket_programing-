#!/bin/python3
import tkinter as tk
win1 = tk.Tk()
win1.title('widget2 demo')
win1.geometry('500x500')

#greet function
def say_hello():
	name = entry.get()
	print(f'Hello, {name}!!, hope you are good')
#label
label= tk.Label(win1, text="Enter Name: ")
label.pack()
#entry
entry = tk.Entry(win1)
entry.pack()


#button
button = tk.Button(win1, text="Say Hello", command=say_hello).pack()

win1.mainloop()
