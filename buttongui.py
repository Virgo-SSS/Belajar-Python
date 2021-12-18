from tkinter import *

root = Tk()

Label(root, text= "Nama").grid(row=0)
Label(root, text="Alamat").grid(row=1)
Entry(root, width= 35).grid(row=0, column=1)
Entry(root, width= 35).grid(row= 1, column=1)

root.mainloop()

