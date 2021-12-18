from tkinter import *

root = Tk()
root.title("Calculator")
e = Entry(root,width=40, borderwidth=3)
e.grid(row = 0, column=0, pady=5, padx=5, columnspan=3)

#Button 0-9
def tombol_angka(number):
    ini = e.get()
    e.delete(0, END)
    e.insert (0, str(ini) + str(number))
   
button1 = Button(root, text="1", padx= 35, pady=20, command= lambda: tombol_angka(1)).grid(row = 1, column= 0)
button2 = Button(root, text="2", padx= 35, pady=20, command= lambda: tombol_angka(2)).grid(row = 1, column= 1)
button3 = Button(root, text="3", padx= 35, pady=20, command= lambda: tombol_angka(3)).grid(row = 1, column= 2)
button4 = Button(root, text="4", padx= 35, pady=20, command= lambda: tombol_angka(4)).grid(row = 2, column= 0)
button5 = Button(root, text="5", padx= 35, pady=20, command= lambda: tombol_angka(5)).grid(row = 2, column= 1)
button6 = Button(root, text="6", padx= 35, pady=20, command= lambda: tombol_angka(6)).grid(row = 2, column= 2)
button7 = Button(root, text="7", padx= 35, pady=20, command= lambda: tombol_angka(7)).grid(row = 3, column= 0)
button8 = Button(root, text="8", padx= 35, pady=20, command= lambda: tombol_angka(8)).grid(row = 3, column= 1)
button9 = Button(root, text="9", padx= 35, pady=20, command= lambda: tombol_angka(9)).grid(row = 3, column= 2)
button0 = Button(root, text="0", padx= 35, pady=20, command= lambda: tombol_angka(0)).grid(row = 4, column= 0)

#tombol delete
def hapus():
    e.delete(0, END)
delete = Button(root, text=" <-", padx=30, pady=20, command = hapus, bg = "red").grid(column = 3, row = 0)

# operator
def tambah():
    first_num = e.get()
    global f_num 
    f_num = int(first_num)
    e.delete(0, END)
penambahan = Button(root, text="+", padx=34, pady=20, command =tambah,bg = "red").grid(column = 3, row = 1 )

# hasil dan delete
def hasil():
    sec_number = e.get()
    e.insert(0,  int(sec_number))
    e.delete(0, END)


equals = Button(root, text="=", padx= 79, pady=20, command= hasil, bg = "blue").grid(column= 1, row= 4, columnspan=2)

kurang =Button(root, text="-", padx=36, pady=20, command =tambah, bg = "red").grid(column = 3, row = 2 )
kali = Button(root, text="X", padx=36, pady=20, command =tambah, bg = "red").grid(column = 3, row = 3 )
bagi = Button(root, text="/", padx=36, pady=20, command =tambah, bg = "red").grid(column = 3, row = 4 )


root.mainloop()

