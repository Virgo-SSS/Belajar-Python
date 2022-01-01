import mysql.connector
from mysql.connector import errorcode

#Dictonary agar mudah dalam pengetikan login
nama_db = {
    'user' : 'root',
    'password': '',
    'host': 'localhost',
    'database' : 'latihann'
}

# koneksi = mysql.connector.connect(**nama_db)

#Pengecekan  error
try:
   koneksi = mysql.connector.connect(**nama_db)
except mysql.connector.Error as mye:
    if mye.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Gagal koneksi ke  database, kesalahan mungkin pada username atau password")
    elif mye.errno == errorcode.ER_BAD_DB_ERROR:
        print("Nama database tidak ditemukan")
    else:
        print("Gagal koneksi ke database")
else:
    print("Koneksi database telah berhasil")

# kursor = koneksi.cursor()


# kursor.execute("DESC mobil")

# for i  in kursor:
#     print(i[0]),
#     print(i[1])

