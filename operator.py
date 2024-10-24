    #Deklarasi Variabel bill = 0
bill = 0
bil2 = 0
jumlah = 0
kurang = 0
kali = 0
bagi = 0
hsl_bagi = 0
sisa_bagi = 0
pangkat = 0

    #Input
bill = int(input("Masukkan Bilangan 1 :"))
bil2 = int(input("Masukkan Bilangan 2 : "))
#Proses
jumlah = bill + bil2 
kurang = bill - bil2
kali = bill * bil2 
bagi = bill / bil2
hsl_bagi = bill // bil2
sisa_bagi = bill % bil2
pangkat = bill ** bil2

    #Output 
print()
print("Hasil penjumlahan    : ", jumlah)
print("Hasil pengurangan    : ", kurang)
print("Hasil perkalian    : ", kali)
print("Hasil pembagian    : ", bagi)
print("Hasil pembagian genap    : ", hsl_bagi)
print("Sisa hasil bagi    : ", sisa_bagi)
print("Hasil perpangkatan    : ", pangkat)