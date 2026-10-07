# Program Manajemen Data Mahasiswa
# Nama    : Aldo Armando Taneo
# NIM     : 257111009
# Jurusan : Pendidikan Informatika

from linked_list import DoubleLinkedList

dll = DoubleLinkedList()

def menu():
    # Memasukkan data awal
    dll.tambah_akhir("257111009", "Aldo Armando Taneo", "Pendidikan Informatika")

    while True:
        print("\n--- PROGRAM MANAJEMEN DATA MAHASISWA ---")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            nim = input("Masukkan NIM: ")
            nama = input("Masukkan Nama: ")
            jurusan = input("Masukkan Jurusan: ")
            dll.tambah_akhir(nim, nama, jurusan)
            print("Data berhasil ditambahkan!")
        elif pilihan == "2":
            dll.tampilkan()
        elif pilihan == "3":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    menu()