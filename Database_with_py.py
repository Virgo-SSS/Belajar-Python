import mysql.connector
from mysql.connector import errorcode

#Dictonary agar mudah dalam pengetikan login
nama_db = {
    'user' : 'root',
    'password': '',
    'host': 'localhost',
    'database' : 'aset'
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


# melakukan koneksi ke localhost database kita
koneksi = mysql.connector.connect(**nama_db)
# perintah cursor digunakan untuk menggunak querry sql  ke python, untuk itu perlu buat 
# variable baru yg dimana, isi nya adalah cursor agar queery sql bisa di jalankan di python
perintah = koneksi.cursor()

# jgn lupa selalu gunakan execute untuk menjalan queery sql nya
#tambahkan print agar kita tau kalau querry sql berhasil di  jalan kan (optional), gk pakai juga gpp

# perintah.execute("Create database aset")
# print("data base berhasil di buat")

# perintah.execute("Drop database aset_kantor")
# print("database berhasil di drop")

# Variable untuk bikin table
# buat_table = """ Create table aset_kantor(
#     kode int not null auto_increment,
#     nama varchar(100),
#     tgl_beli date,
#     merek varchar(100),
#     nilai  decimal(15,2),
#     primary key(kode)
# ) engine = innodb
# """

# buat_table2 = """ Create table aset_kantor2(
#     kode int not null auto_increment,
#     nama varchar(100),
#     tgl_beli date,
#     merek varchar(100),
#     primary key(kode)
# ) engine = innodb
# """

#kemudian execute untuk melakukan querry variable buat table
# perintah.execute(buat_table2)
# print("table berhasil di buat")

# perintah.execute("show tables")
# for i in perintah: #perulangan untuk menampilkan banyak nya tables
#     print(i)

perintah.execute("desc aset_kantor")
for i in perintah:
    print(i[0],i[1], i[2], i[3], i[4], i[5]) 
    #[0],[1], itu merupakan index dari isi field 
    # [0] -> nama kolom
    # [1] -> tipe data
    # [2] -> null atau not null
    # [3] -> tipe key,
    # [4] -> default 
    # [5] -> extra 

    
