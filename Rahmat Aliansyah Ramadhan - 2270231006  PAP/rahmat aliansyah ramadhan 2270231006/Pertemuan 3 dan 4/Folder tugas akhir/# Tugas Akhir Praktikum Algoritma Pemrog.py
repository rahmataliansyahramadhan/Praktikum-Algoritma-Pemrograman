# Tugas Akhir Praktikum Algoritma Pemrograman
# Create by ASLAB ELITS 2022

"""
Kasir Pasar Cabe

Program ini berfungsi untuk melakukan pencetakan bon transaksi Pasar Cabe. Program akan 
meminta memasukan identitas customer, kemudian menghitung biaya dari Pasar Cabe tersebut dan
mencetak bon hasil transaksi.
"""
import datetime

identitas = ["Nama Pelanggan", "Alamat", "No Telepon", "Berat", "Kategori"]
data = []
biayaLayanan = 0
tanggal = datetime.datetime.now()

print(30*"="+"""
Nama\t: Rahmat Aliansyah Ramadhan
NIM\t: 2270231006
Program\t: Pasar Cabe
""" + 30*"=" + "\n")

for x in range(len(identitas)):
    val = input("Masukkan " + identitas[x] + ": ")
    data.append(val)

kategori = str(data[4]).upper()

if(kategori == "CABE HIJAU"):
    biayaLayanan = 80000* int(data[3])
elif(kategori == "CABE MERAH"):
    biayaLayanan = 150000 * int(data[3])
else:
    print("Harap masukkan layanan kategori")

print("\n"+8*"=" + "Transaksi Pasar Cabe" + 8*"="+"\n") 

print("Tanggal : " + tanggal.strftime("%d - %m - %Y %X"))

for x in range(4):
    print(identitas[x] + " : " + data[x])

if(biayaLayanan % 8000 == 0):
    print("Kategori : 80000/Kg")
else:
    print("Kategori: 150000/Kg")
print("Total biaya: " + str(biayaLayanan))