from mainwarung import Queue

def MainMenu():
    q = Queue();

    produk_list = [
        {"nomer": "1", "nama": "Roti Tawar", "harga": 10000},
        {"nomer": "2", "nama": "Susu Coklat", "harga": 15000},
        {"nomer": "3", "nama": "Air Oemboel", "harga": 5000},
        {"nomer": "4", "nama": "RTX 3080", "harga": 250000},
        {"nomer": "5", "nama": "Asus TUF", "harga": 500000}
        ];
    
    while True:
        print("=== Waroeng Smart Madura ===");
        print("1. Tambah Pelanggan");
        print("2. Layani Pelanggan");
        print("3. Keluar Aplikasi");

        pilih = input("Pilih 1-3 : ");

        if pilih == "1":
            nama = input("Nama pelanggan : ");
            q.Enqueue(nama);
            print(f"{nama} masuk antrian.");
        elif pilih == "2":
            if q.IsEmpty():
                print("Antrian kosong.");
            else:
                nama = q.Dequeue();
                print(f"Melayani {nama}");
                print("=== Daftar Produk Waroeng Madura ===");
                for p in produk_list:
                    print(f"{p['nomer']}.  {p['nama']}  Rp {p['harga']}");

                total = 0;
                while True:
                    nomer = input("Nomer produk (isi b untuk bayar): ")
                    if nomer == "b":
                        print(f"Total belanja {nama}: Rp {total:,d}")
                        while True:
                            bayar = input("Bayar: ")
                            try:
                                bayar = int(bayar)
                                if bayar < total:
                                    print("Uang kurang")
                                else:
                                    kembalian = bayar - total
                                    print(f"Terima kasih. Kembalian: Rp {kembalian:,d}")
                                    break
                            except ValueError:
                                print("Masukkan jumlah uang yang valid.")
                        break

                    for p in produk_list:
                        if p["nomer"] == nomer:
                            total += p["harga"]
                            print(f"{p['nama']} ditambahkan. Total: Rp {total:,d}")
                            break
                    else:
                        print("Nomer tidak valid.")


                    
        elif pilih == "3":
            print("Program selesai.");
            break
        else:
            print("Pilihan tidak valid.");  

if __name__ == "__main__":
    MainMenu()