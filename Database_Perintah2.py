#INI ADALAH KUMPULAN KUMPULAN QUERY MYSQL DI PYTHON, JGN DI RUN HANYA SEBAGAI TEXT
# UNTUK "PERINTAH", JGN LUPA DI GANTI SESUAI NAMA VARIABLE CURSOR MASING2

'''Bikin Database'''
# perintah.execute("Create database latihanPY")
# print("data base berhasil di buat")

'''Drop database'''
# perintah.execute("Drop database aset")
# print("database berhasil di drop")

'''Show database'''
# perintah.execute("Show databases")
# for i in perintah:
#     print (i)


'''BIKIN table'''
'''Variable untuk bikin table'''
# buat_table = """ Create table aset_kantor(
#     kode int not null auto_increment,
#     nama varchar(100),
#     tgl_beli date,
#     merek varchar(100),
#     nilai  decimal(15,2),
#     primary key(kode)
# ) engine = innodb
# # """

# buat_table2 = """ Create table aset_kantor2(
#     kode int not null auto_increment,
#     nama varchar(100),
#     tgl_beli date,
#     merek varchar(100),
#     primary key(kode)
# ) engine = innodb
# """

# perintah.execute(buat_table2)
# print("table berhasil di buat")
'''kemudian execute untuk melakukan querry variable buat table'''

''' Show tables'''
# # perintah.execute("show tables")
# # for i in perintah: #perulangan untuk menampilkan banyak nya tables
# #     print(i)

''' Desc table'''
# perintah.execute("desc aset_kantor")
# for i in perintah:
#     print(i[0],i[1], i[2], i[3], i[4], i[5]) 
'''[0],[1], dst itu merupakan index dari table kita
[0] -> field
[1] -> type (tipe data)
[2] -> null atau not null
[3] -> tipe key,
[4] -> default 
[5] -> extra '''

'''insert table'''
# data = "insert into customers(nama, adrres) values( %s, %s)"
# isi_data =  [
#     ('virgo','jalan durian'),
#     ('stevanus','jalan belimbing'),
#     ('kristina','jalan duku'),
#     ('miranda','jalan buah'),
#     ('sinaga','jalan jalan')
# ]
# for i in isi_data:
#     perintah.execute(data, i)
#     koneksi.commit() #nama "koneksi" tergantung dari nama variable untuk koneksi ke local host
# print("Berhasil memasukan data")

'''Menampilkan data'''
# perintah.execute("Select * from  customers")
# for i in perintah:
#     print(i)

'''Mengupdate data'''
# update_data = "update customers set nama =%s, adrres=%s where customers_id =%s "
# isi_data = ('vir','jalan bar',18)
# perintah.execute(update_data, isi_data)
# koneksi.commit() #nama "koneksi" tergantung dari nama variable untuk koneksi ke local host
# print("Data berhasil di update")

'''Delet data'''
# delete_data = "delete from customers where customers_id = %s"
# data = (18, )
# perintah.execute(delete_data, data)
# koneksi.commit()
# print("Data berhasil di hapus")