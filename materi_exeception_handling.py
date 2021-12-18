try:
    angka = int(input("masukan angka antara 10 sampai 20 "))
except ValueError:
    print("anda harus memasukan angka dari 10 sampai 20 saja")
else:
    if (angka >= 10) and (angka <= 20):
        print("angka yang anda masukan adalah ", angka)
    else:
        print("angka anda diluar rentang 1- dn 20 !")