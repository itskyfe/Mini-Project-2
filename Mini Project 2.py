from prettytable import PrettyTable

tabel = PrettyTable()
tabel.field_names = ["tgl masuk barang", "Nama pemilik", "tgl keluar barang"]
paket = []

for p in range(len(paket)):
    tabel.add_row([paket[p][0], paket[p][1], paket[p][2]])

def tampil_data():
    print("\n")
    if len(paket) <= 0:
        print ("============= Belum Ada data =============")
    else:
        print(tabel)

def tambah_data():
    tgl_masuk = input("Masukkan tanggal masuk barang (dd/mm/yyyy) : ")
    nama = input("Masukkan nama pemilik barang : ")
    tgl_keluar = input("Masukkan tanggal masuk barang (dd/mm/yyyy)/ (beri strip (-) kalau barang belum keluar): ")
    paket.append([tgl_masuk, nama, tgl_keluar])
    tabel.add_row([tgl_masuk, nama, tgl_keluar])
    print("\n")
    print("======= Data berhasil ditambahkan =======")
    tampil_data()

def update_data():
    print(tabel)
    print("========== Update data barang ==========")
    nama = input("Masukkan nama pemilik barang yang datanya ingin diupdate: ")
    for id, item in enumerate(paket):
        if item[1] == nama:
            update = input("Masukkan tanggal keluar barang: ")
            paket[id][2] = update
            tabel.clear_rows()
            for packet in paket:
                tabel.add_row(packet)
            print("========== Data berhasil diubah ==========")
        else:
            print("============= Data tidak ada =============")
    tampil_data()

def hapus_data():
    print(tabel)
    print("========== Hapus data barang ==========")
    nama = input("Masukkan nama pemilik barang yang datanya ingin dihapus: ")
    for id, item in enumerate(paket):
        if item[1] == nama:
            del paket[id]
            tabel.clear_rows()
            print("========== Data berhasil dihapus ==========")
        else:
            print("============= Data tidak ada ==============")
    print(tabel)

def pilih_role():
    while True:
        print("==== Pilih role anda ====")
        print("[1] Saya adalah admin")
        print("[2] Saya adalah customer")
        print("[3] Keluar")
        print("=========================")
        opsi = input("Pilihan Anda: ")
        if opsi == "1":
            menu_admin()
        elif opsi == "2":
            menu_customer()
        elif opsi == "3":
            print("Terima kasih! Have a nice day^^")
            break
        else:
            print("Pilihan tidak ada")

def menu_admin():
    user = input("Masukkan Username Anda : ")
    pass1 = input("Masukkan Password Anda : ")
    pass2 = input("Konfirmasikan Password Anda : ")
    if pass1 == pass2:
        print("\n")
        print(f"+ Selamat Datang {user}, Semangat ya hari ini +")
        print("\n")
        while True:    
            print("================ Gudang JNT ================")
            print("[1] Tampil Data Barang")
            print("[2] Tambah Data Barang")
            print("[3] Update Data Barang")
            print("[4] Hapus Data Barang")
            print("[5] Keluar dari Menu Admin")
            print("============================================")
            pilihan = int(input("Masukkan Pilihan Anda: "))
            if pilihan == 1:
                tampil_data()
            elif pilihan == 2:
                tambah_data()
            elif pilihan == 3:
                update_data()
            elif pilihan == 4:
                hapus_data()
            elif pilihan == 5:
                print("Keluar dari menu admin.")
                break
            else:
                print("Pilihan Anda salah.")
    else:
        print("Password anda salah.")

def menu_customer():
    while True:
        print("==================== Menu Customer ====================")
        print(tabel)
        pilihan = input("Apakah anda ingin keluar? (y/n)")
        
        if pilihan.lower() == "y":
            print("Terima kasih! Have a nice day^^")
            break

if __name__ == "__main__":
    pilih_role()