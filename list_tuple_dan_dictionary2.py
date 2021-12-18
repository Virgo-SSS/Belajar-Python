#lanjutan dari list_tuple_dictionary

# fungsi list
# print(list("joni gudel")) #akan menghasil kan sebuah list yang dipisah2 sesuai urutan index

# #contoh pengunaan list lagi
pertanyaan = int(input("Sebutkan bulan keberapa (1 - 12) ?"))
bulan = ['januari','feburary','maret', 'april', 'mei', 'juni', 'juli', 'agustus', 'september','oktober', 'november', ' desember']

if 1 <= pertanyaan <= 13:
    print("Bulan", bulan [pertanyaan - 1]) #di kurangin 1 karena index di mulai dari 0, jadi biar tepat hitung nya di kurangin 1

# Bekerja dengan list menggunakan beberapa fungsi
# append digunakan untuk menambahkan data baru di bagian akhir list
# len mengembalikan jumlah data dalam list
# index memberi tahu lokasi data yang ada dalam list
#del dapat digunakan untuk menghapus data tertentu dalam list
# sort digunakan  untuk mengurutkan list
# Contoh 

menu_item = 0
namelist = [] #tidak ada isi berarti index masih 0, ingat di list 
#yang di hitung adlah index yang di mulai dari 0

# membuat perulangan 
while menu_item != 5 :
    print("--------------------------------")
    print("1. Mencetak list")
    print("2. Menbambahkan nama ke dalam list")
    print("3. Menghapus nama dari list")
    print("4. Mengubah data dalam list")
    print("5. keluar")
    menu_item = int(input("pilih menu :")) #membuat input untuk variable menu__item
    if menu_item == 1: #membuat program untuk no 1
        current = 0
        if len(namelist) > 0: #jika jumlah data di name list di atas 0, lakukang while
            while current < len(namelist):
                print(current, ".", namelist[current])
                current = current + 1
        else:
            print("list kosong")
    elif menu_item == 2: #membuat program untuk no 2
        name = input ("masukan nama :")
        namelist.append(name)
    elif menu_item == 3: #membuat program untuk no 3
        del_name = input("nama yang ingin di hapus :")
        if del_name in namelist:
            item_number = namelist.index(del_name)
            del namelist[item_number]
        else:
            print(del_name, "tidak di temukan")
    elif menu_item == 4: #membuat program untuk no 4
        old_name = input("Nama apa yang ingin di ubah :")
        if old_name in namelist:
            item_number = namelist.index(old_name)
            new_name = input("nama baru :")
            namelist[item_number] = new_name
        else:
            print(old_name, "tidak ditemukan")

print("Selamat tinggal")

