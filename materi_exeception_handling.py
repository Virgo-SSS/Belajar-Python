""" ini adalah format comment, format comment ada 2 untuk python yg pertama "#" dan kedua yg sedang di gunakan ini

Mengatasi masalah dengan exception handling
contoh kita meminta user untuk menginput angka dari 10 sampai 20. ternyata user menginput 21.
jika tidak kita antisipasi, kesalah ini menyebabkan program tidak bekerja dengan baik

contoh nya adalah kodingan di bawah
hampir sama seperti if dan elif
"""
 #kita menggukanan perulangan untuk masalah ini, jadi ketika 
while True : 
    try:
        angka = int(input("masukan angka antara 10 sampai 20 :"))
    #execpt itu pengecualian, jadi ketika kita meminta user menginput sebuah int, tetapi user 
    # malah menginput string maka akan di tampilkan except value error dan program akan mengulang  lagi ke try
    except ValueError: 
        print("anda harus memasukan angka dari 10 sampai 20 saja")
    # jika user sudah benar menginput int, maka excpet value error akan di abaikan dan akan di lanjut kan ke else
    # di else kita punya sebuah nested if
    # karena kita meminta rentang angka 10 - 20, maka kita membuat if seperti di bawah
    # kemduian jika user menginput angka diluar 10 - 20 maka program akan menjalankan else dan 
    # program akan mengulang try
    # jika user menginput angka dari 10 - 20 maka program akan menjalankan if dan break sebagai command untuk menghentikan looping
    else:
        if (angka >= 10) and (angka <= 20):
            print("angka yang anda masukan adalah ", angka)
            break
        else:
            print("angka anda diluar rentang 1 dan 20 !")