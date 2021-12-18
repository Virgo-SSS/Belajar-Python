# Urutan index di mulai dari 0,1,2,3 ds
# sequence(struktur data) punya beberapa jenis, contoh nya list dan tuples
# list  di tandai dengan [ ]

# contoh sequence( struktur data) menggunakan list
joni = ['joni guide', 27]
mimin =['mimin item', 12]
database = [joni, mimin]
print(database)

#======================================================================================
#indexing
#setiap sequence (struktur data) di beri nomor urut (index) yang di mulai dari 0
# contoh
nama = "Joni Gudel"
#index pada variable nama : J = 0, o = 1, n = 2, i = 3, dst
print(nama[0])
#jika kita memanggil variable nama dan disini dengan index 0, maka huruf J akan kepanggil
print(nama[1])
#jika kita mengisi nomor index dengan 1 maka yg terpanggil ada huruf o
print(nama[-1])
# kita juga bisa mengisi index dengang -1, maka program akan membaca nya dari kanan, jadi -1 maka huruf l akan terpanggil

print("Joni Gudel"[1]) # dan sebenanrya untuk tipe data string kita bisa tidak membuat variable nama nya
# kita bisa langsng seperti kodingan di atas lgsng menulis nomor index yang mau kita panggil

#===============================================================================================
#Slicing
#digunakan untuk mengakses beberapa elemen sekaligus,
#slicing  harus di isi dengan 2 nomor index yaitu awal dan akhir [awal:akhir] (sama seperti range)
print(nama [0:4]) #index dari 0 sampai 4, akan menghasil kan joni
#slicing juga bisa di di tambakan jarak huruf yg mau di ambil (beda)
print(nama[0:7:3]) # 0 itu awal index, 7 akhir index, dan 3 adalah jarak nya


# sekian materi mengenai sequence

"""Fungsi fungsi pada python untuk list
1. append() di gunakan untuk menambah isi list
2. clear () digunakan untuk menghapus seluru isi list
3. copy() digunakan untuk membuat salinan dari sebuah list ke list lain yg baru
4. extend() menambah item dari list lain ke dalam list yang sudah ada
5. insert() menambah item ke posisi tertenu dalam sebuah list
6. pop () menghapus isi terakhir di dalam list
7. remove() menghapus isi list yang di tentukan berdasarkan posisi nya
"""