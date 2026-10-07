class Node:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_akhir(self, nim, nama, jurusan):
        node_baru = Node(nim, nama, jurusan)
        if not self.head:
            self.head = node_baru
            self.tail = node_baru
        else:
            self.tail.next = node_baru
            node_baru.prev = self.tail
            self.tail = node_baru

    def tampilkan(self):
        if not self.head:
            print("Belum ada data mahasiswa.")
            return
        
        saat_ini = self.head
        no = 1
        print("\n=== DAFTAR MAHASISWA ===")
        while saat_ini:
            print(f"{no}. NIM: {saat_ini.nim} | Nama: {saat_ini.nama} | Jurusan: {saat_ini.jurusan}")
            saat_ini = saat_ini.next
            no += 1