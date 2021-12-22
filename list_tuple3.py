#fungsi len() untuk menampilkan jumlah banyak nya data
list2 = []
print("isi list2 adalah:", len(list2))

# fungsi append() untuk menambah kan data 
list2.append('joni')
print("sekarang isi list2 ada : ", len(list2), "item")
print("yaitu : ", list2[0])

#fungsi insert() untuk menambah data dan meletakan nya di index tertentu
list2.insert(1, 'siti')
print("ini anggota-anggota baru di list, yaitu:", list2)

# Fungsi copy() untuk mengcopy salinan list lain 
list3 = list2.copy()
print("isi list 3 yaitu,", list3)

#fungsi extend() menambahkan isi seluruh list ke dalam ke list lain
list2.extend(list3)
print("Gabungan list 2 dan 3 adalah : ", list2)

# funsi pop() untuk menghapus item terakhir di dalam list
list2.pop()
print(list2)

#fungsi clear() untk menghapus seluruh item 
list3.clear()
print(len(list3))