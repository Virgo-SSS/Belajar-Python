from tkinter import *
import time
from time import strftime

root = Tk()
root.resizable = (False, False)
root.title=("Jam buatan saya")

def waktu():
    string = strftime('%H:%M:%S')
    Label.config(text = string)
    Label.after(1000,time)

Label = Label(root, 
            font = ('calibri', 40, 'bold'),
            background= 'blue',
            foreground='white')

Label.pack(anchor='center')

time()
mainloop()