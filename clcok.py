from tkinter import *
from tkinter.ttk import *

from time import strftime


root = Tk()
root.title("Clock")


label = Label(root, font=("Arial", 80), background="black", foreground='green')
label.pack(anchor='center')


mainloop()
