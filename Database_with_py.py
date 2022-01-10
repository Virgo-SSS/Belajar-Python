import mysql.connector
from mysql.connector import errorcode

#Dictonary agar mudah dalam pengetikan login
nama_db = {
    'user' : 'root',
    'password': '',
    'host': 'localhost',
    'database' : 'latihanPY'
}

# melakukan koneksi ke localhost database kita
koneksi = mysql.connector.connect(**nama_db)

#Pengecekan  error (jangan lupa variable koneksi di atas di jadikan comment terlebih dahulu)
# try:
#    koneksi = mysql.connector.connect(**nama_db)
# except mysql.connector.Error as mye:
#     if mye.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Gagal koneksi ke  database, kesalahan mungkin pada username atau password")
#     elif mye.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Nama database tidak ditemukan")
#     else:
#         print("Gagal koneksi ke database")
# else:
#     print("Koneksi database telah berhasil")
#     koneksi.close()

# # perintah cursor digunakan untuk menggunak querry sql  ke python, untuk itu perlu buat 
# # variable baru yg dimana, isi nya adalah cursor agar queery sql bisa di jalankan di python
perintah = koneksi.cursor()

# jgn lupa selalu gunakan execute untuk menjalan queery sql nya
#tambahkan print agar kita tau kalau querry sql berhasil di  jalan kan (optional), gk pakai juga gpp


    
