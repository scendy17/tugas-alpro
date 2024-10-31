# input watt perbarang
daya_kipas = int(input("watt kipas: ")) 
daya_tv = int(input("watt TV: "))        
daya_lampu = int(input("watt lampu: "))  

# input waktu penggunaan perbarang
waktu_kipas = int(input(" waktu penggunaan kipas: ")) 
waktu_tv = int(input("waktu penggunaan tv: "))       
waktu_lampu = int(input("waktu penggunaan lampu: "))  

#  harga per 1 kwh
hargakwh = 1500

# proses
konsumsi_kipas = daya_kipas * waktu_kipas
konsumsi_tv = daya_tv * waktu_tv
konsumsi_lampu = daya_lampu * waktu_lampu

#  total watt perjam
total_konsumsi_watt = konsumsi_kipas + konsumsi_tv + konsumsi_lampu

#  konversi wh ke kwh
total_konsumsi_kwh = total_konsumsi_watt / 1000

# harga 1 hari 
total_harga = hargakwh * total_konsumsi_kwh

# total harga selama 1 bulan
harga_perbulan = total_harga * 30

#  hasil
print(f" total watt barang: {total_konsumsi_watt:} Wh")
print(f" total kwh barang: {total_konsumsi_kwh:} kWh")
print(f" total harga perhari: Rp.{total_harga:} ")
print(f" total harga dalam satu bulan: Rp.{harga_perbulan:} ") 