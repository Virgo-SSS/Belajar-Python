from tkinter import *

root = Tk()
root.title("Volume segitiga")
root.geometry("200x200")
Label(root, text = " Volume Segitiga").grid(row=  0, column=1,columnspan=2, sticky=W)
Label(root, text = " ").grid(row=  1)
Label(root, text= "Panjang").grid(row=3)
Label(root, text="Lebar").grid(row=4)
Label(root, text="Tinggi").grid(row=5)

#Hasil input panjang, lebar, tinggi masuk ke sini sebagai integer
data1 =  IntVar()
data2 = IntVar()
data3 = IntVar()

# kolom input panjang,lebar, tinggi
panjang = Entry(root,textvariable = data1, width= 20).grid(row=3,padx= 3, column=1, columnspan=2)
lebar = Entry(root, textvariable = data2, width= 20).grid(row= 4,padx=3, column=1, columnspan=2)
tinggi = Entry(root, textvariable = data3, width= 20).grid(row=5,padx=3, column=1, columnspan=2)

# Label untuk jawaban
kosong = Label(root,font=('arial',11), fg ='blue')
kosong.grid(row = 9, column=0, columnspan=2, sticky =W)

#rumus
def rumus():
    hasil = int(1*data1.get()*data2.get()*data3.get()/2)
    kosong.config(text = "volume segitiga : "+ str(hasil)+ " cm³")

#button hasil
mybutton = Button(root,text = "Hasil", command= rumus).grid(row = 6, column = 1)

root.mainloop()

