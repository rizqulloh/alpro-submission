from src import fs
import os

products = fs.Filesystem(os.getcwd() + "/data/products.csv")


class Product:
    def __init__(self):
        self.data = products.loadData()

    def showProducts(self):
        if len(self.data) == 0:
            print("\n|==============================|")
            print("|                              |")
            print("|Tidak ada produk yang tersedia|")
            print("|                              |")
            print("|==============================|")
        else:
            print("\nBerikut adalah produk yang tersedia: \n")
            iterate = 0
            for product in self.data:
                iterate += 1
                print(f"{iterate}. Nama Produk  :{product['name']}")
                print(f"   Kategori \t:{product['category']}")
                print(f"   Harga: \t:{product['price']}")
                print(f"   Stok: \t:{product['stock']}")

        print("\nNavigasi: ")
        print("0. Halaman Utama")
        print("12. Tambah Produk Baru")
        print("13. Lihat Detail Produk")
        print("14. Edit Produk")
        print("15. Hapus produk\n")

    def createProduct(self):
        newProduct = {}
        print("\nLengkapi permintaan dibawah ini")
        newProduct["name"] = input("Nama produk: ")
        newProduct["category"] = input("Kategori: ")
        newProduct["price"] = input("Harga: ")
        newProduct["stock"] = input("Stok: ")

        products.write(newProduct)

        oldSize = len(self.data)
        self.data = products.loadData()

        if len(self.data) > oldSize:
            print("Produk berhasil ditambahkan!!")

        print("\nNavigasi: ")
        print("0. Halaman Utama")
        print("1. Lihat semua produk")
        print("13. Lihat Detail Produk")
        print("14. Edit Produk")
        print("15. Hapus Produk\n")

    def showProduct(self):
        param = input("Nama produk: ")
        available = False
        for data in self.data:
            if data["name"] == param:
                print("\nDetail Produk: ")
                print("Nama produk: ", data["name"])
                print("Kategori: ", data["category"])
                print("Stok: ", data["stock"])
                available = True
                break

        if available == False:
            print("Maaf, produk tidak ditemukan")

        print("\nNavigasi: ")
        print("0. Halaman Utama")
        print("1. Lihat semua produk")
        print("12. Tambah produk baru")
        print("14. Edit Produk")
        print("15. Hapus Produk\n")

    def editProduct(self):
        param = input("Nama produk: ")
        available = False
        for data in self.data:
            if data["name"] == param:
                newDict = {}
                newDict["name"] = input("Nama produk terbaru: ")
                newDict["category"] = input("Kategori: ")
                newDict["price"] = input("Harga: ")
                newDict["stock"] = input("Stok: ")
                products.update(newDict, "name", param)
                print("\nProduk diperbarui")
                self.data = products.loadData()
                available = True
                break

        if available == False:
            print("Maaf, produk tidak ditemukan")

        print("\nNavigasi: ")
        print("0. Halaman utama")
        print("1. Lihat semua produk")
        print("12. Tambah produk Baru")
        print("13. Lihat detail produk\n")
        print("15. Hapus produk")

    def deleteProduct(self):
        param = input("Nama Produk: ")
        available = False
        for data in self.data:
            if data["name"] == param:
                oldData = len(self.data)
                products.delete("name", param)
                self.data = products.loadData()

                if len(self.data) < oldData:
                    print("Data berhasil dihapus")

                available = True

        if available == False:
            print("Maaf, produk tidak ditemukan")

        print("\nNavigasi: ")
        print("0. Halaman utama")
        print("1. Lihat semua produk")
        print("12. Tambah produk Baru")
        print("13. Lihat detail produk")
        print("14. Edit produk\n")
