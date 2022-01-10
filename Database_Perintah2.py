#INI ADALAH KUMPULAN KUMPULAN PERINTAH MYSQL DI PYTHON, JGN DI RUN HANYA SEBAGAI TEXT

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
# perintah.execute("""
#     insert into aset_kantor(nama, tgl_beli, merek, nilai) values
#     ('Virgo', '2021-01-01', 'toyoya', 15),
#     ('stevanus', '2021-02-01', 'toyoya', 15)
# """)
