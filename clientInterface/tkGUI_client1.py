from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry('100x200')

def hellocallback(event):
	msg = messagebox.showinfo('hello python','hello world')
	B = Button(top, text= 'Hello')
	B.place(x=10, y=40)



top.mainloop()
