# Data awal kursus
kursus = [
    {"nama": "Coding Python", "harga": 50000, "umur_min": 12, "gender": "semua", "pendaftar": []},
    {"nama": "Coding C++", "harga": 50000, "umur_min": 12, "gender": "semua", "pendaftar": []},
    {"nama": "Coding PHP", "harga": 50000, "umur_min": 12, "gender": "semua", "pendaftar": []},
    {"nama": "Coding JavaScript", "harga": 50000, "umur_min": 12, "gender": "semua", "pendaftar": []},
    {"nama": "Logika Pemrograman", "harga": 100000, "umur_min": 10, "gender": "semua", "pendaftar": []},
    {"nama": "PTIK", "harga": 1000000, "umur_min": 10, "gender": "semua", "pendaftar": []},
]

# Kredensial admin
admin_cred = {"username": "admin", "password": "admin123"}

# Fungsi menampilkan daftar kursus
def tampilkan_kursus():
    print("\nDaftar Kursus:")
    for idx, kursus_item in enumerate(kursus, start=1):
        print(f"{idx}. {kursus_item['nama']}, Harga: Rp{kursus_item['harga']}/hari, Umur {kursus_item['umur_min']}+, Gender: {kursus_item['gender']}")

# Fungsi untuk admin melihat data kursus beserta pendaftarnya
def lihat_data_kursus():
    print("\n===== DATA KURSUS =====")
    for idx, kursus_item in enumerate(kursus, start=1):
        print(f"{idx}. {kursus_item['nama']}")
        print(f"   Harga: Rp{kursus_item['harga']}/hari, Umur {kursus_item['umur_min']}+, Gender: {kursus_item['gender']}")
        if kursus_item["pendaftar"]:
            print("   Pendaftar:")
            for pendaftar in kursus_item["pendaftar"]:
                print(f"      - Nama: {pendaftar['nama']}, Umur: {pendaftar['umur']}, Gender: {pendaftar['gender']}")
        else:
            print("   Belum ada pendaftar.")
    print("\n=========================")

# Fungsi CRUD untuk admin
def admin_menu():
    while True:
        print("\n===== MENU ADMIN =====")
        print("1. Lihat Data Kursus dan Pendaftar")
        print("2. Tambah Kursus (Create)")
        print("3. Ubah Kursus (Update)")
        print("4. Hapus Kursus (Delete)")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_data_kursus()
        elif pilihan == "2":
            tambah_kursus()
        elif pilihan == "3":
            ubah_kursus()
        elif pilihan == "4":
            hapus_kursus()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

def tambah_kursus():
    print("\nTambah Kursus Baru")
    nama = input("Nama Kursus: ")
    harga = int(input("Harga Kursus: "))
    umur_min = int(input("Umur Minimal: "))
    gender = input("Gender (pria/wanita/semua): ").lower()
    kursus.append({"nama": nama, "harga": harga, "umur_min": umur_min, "gender": gender, "pendaftar": []})
    print(f"Kursus '{nama}' berhasil ditambahkan!")

def ubah_kursus():
    tampilkan_kursus()
    try:
        idx = int(input("\nPilih nomor kursus yang ingin diubah: ")) - 1
        if idx < 0 or idx >= len(kursus):
            print("Nomor tidak valid.")
            return
        kursus_item = kursus[idx]
        print(f"\nMengubah kursus: {kursus_item['nama']}")
        nama = input("Nama Kursus Baru (kosongkan untuk tidak mengubah): ")
        harga = input("Harga Baru (kosongkan untuk tidak mengubah): ")
        umur_min = input("Umur Minimal Baru (kosongkan untuk tidak mengubah): ")
        gender = input("Gender Baru (kosongkan untuk tidak mengubah): ").lower()

        if nama:
            kursus_item["nama"] = nama
        if harga:
            kursus_item["harga"] = int(harga)
        if umur_min:
            kursus_item["umur_min"] = int(umur_min)
        if gender:
            kursus_item["gender"] = gender

        print("Kursus berhasil diperbarui!")
    except ValueError:
        print("Input tidak valid.")

def hapus_kursus():
    tampilkan_kursus()
    try:
        idx = int(input("\nPilih nomor kursus yang ingin dihapus: ")) - 1
        if idx < 0 or idx >= len(kursus):
            print("Nomor tidak valid.")
            return
        kursus_item = kursus.pop(idx)
        print(f"Kursus '{kursus_item['nama']}' berhasil dihapus!")
    except ValueError:
        print("Input tidak valid.")

# Fungsi untuk pengguna mendaftar kursus
def daftar_kursus():
    print("\n===== PENDAFTARAN KURSUS =====")
    nama = input("Masukkan nama Anda: ")
    umur = int(input("Masukkan umur Anda: "))
    gender = input("Masukkan gender Anda (pria/wanita): ").lower()

    kursus_tersedia = [k for k in kursus if umur >= k["umur_min"] and (k["gender"] == "semua" or k["gender"] == gender)]
    if not kursus_tersedia:
        print("Maaf, tidak ada kursus yang cocok.")
        return

    print("\nKursus Tersedia:")
    for idx, k in enumerate(kursus_tersedia, start=1):
        print(f"{idx}. {k['nama']} - Rp{k['harga']}/hari")

    total_biaya = 0
    while True:
        pilihan = int(input("\nPilih nomor kursus (0 untuk selesai): "))
        if pilihan == 0:
            break
        if pilihan < 1 or pilihan > len(kursus_tersedia):
            print("Nomor kursus tidak valid.")
            continue

        hari = int(input(f"Berapa hari untuk kursus {kursus_tersedia[pilihan - 1]['nama']}? "))
        biaya = kursus_tersedia[pilihan - 1]["harga"] * hari

        # Diskon 5% jika durasi lebih dari 20 hari
        if hari > 20:
            diskon_hari = biaya * 0.05
            biaya -= diskon_hari
            print(f"Diskon 5% karena durasi lebih dari 20 hari! Diskon: Rp{diskon_hari}")

        total_biaya += biaya

        # Menambahkan data pendaftar ke kursus yang dipilih
        kursus_tersedia[pilihan - 1]["pendaftar"].append({"nama": nama, "umur": umur, "gender": gender})

        print(f"Kursus {kursus_tersedia[pilihan - 1]['nama']} ditambahkan. Biaya: Rp{biaya}")

    # Memberikan diskon jika total biaya melebihi Rp500.000
    if total_biaya > 500000:
        diskon = total_biaya * 0.1
        total_biaya -= diskon
        print(f"\nAnda mendapatkan diskon 10%! Total diskon: Rp{diskon}")

    print("\n===== RINCIAN PEMBAYARAN =====")
    print(f"Total Biaya: Rp{total_biaya}")
    print("Silakan lakukan pembayaran ke rekening: 123-456-7890 (Bank XYZ).")

# Menu Utama
while True:
    print("\n===== MENU UTAMA =====")
    print("1. Saya Admin")
    print("2. Saya Pengguna")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        username = input("Masukkan username admin: ")
        password = input("Masukkan password admin: ")
        if username == admin_cred["username"] and password == admin_cred["password"]:
            print("Login berhasil sebagai admin!")
            admin_menu()
        else:
            print("Username atau password salah.")
    elif menu == "2":
        daftar_kursus()
    elif menu == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
