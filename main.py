from src import product as p
import os
import sys

Product = p.Product()


def main():
    print("Selamat datang di program CRUD sederhana ini\ndibuat oleh: rizqulloh")
    print("\nBerikut adalah opsi yang dapat anda pilih: ")
    print("|=============================|")
    print("|1. Produk                    |")
    print("|2. Keluar                    |")
    print("|=============================|")


currentPage = 0
while True:
    os.system("clear")

    if currentPage == 0:
        main()
    elif currentPage == 1:
        print("Halaman saat ini: Lihat Semua Produk")
        Product.showProducts()
    elif currentPage == 12:
        print("Halaman saat ini: Tambah produk baru")
        Product.createProduct()
    elif currentPage == 13:
        print("Halaman saat ini: Lihat detail produk")
        Product.showProduct()
    elif currentPage == 14:
        print("Halaman saat ini: Edit produk")
        Product.editProduct()
    elif currentPage == 15:
        print("Halaman saat ini: Hapus produk")
        Product.deleteProduct()
    elif currentPage == 2:
        print("Terima kasih!!")
        sys.exit()

    currentPage = int(input("\nPilihan anda: "))
