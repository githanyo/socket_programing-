import tkinter as tk
root = tk.Tk()
root.geometry('400x400')
root.title('Widgets Demo')


#label
label= tk.Label(root, text="Enter Name: ")
label.pack()
#entry box
entry = tk.Entry(root)
entry.pack()

#button
def say_hello():
	name = entry.get()
	print(f'hello, {name}!!')

button = tk.Button(root, text='Say Hello', command=say_hello).pack()
root.mainloop()
