print("====================================================================")
print("                     PROGRAM MENGHITUNG GAJI                        ")
print("====================================================================")

# input
nama_karyawan = input("masukan nama karyawan\ :")
gaji_pokok = int(input("masukan gaji pokok \ :"))
jam_kerja = int(input("masukan jumlah jam kerja\ :"))
Perjam_lembur = 20000
tunjangan = 0.20  # Tetapkan tunjangan sebagai float
pajak = 0.10  # Tetapkan pajak sebagai float

# proses
# proses perhitungan tunjangan 20%
''
if tunjangan == 0.20:
    besar_tunjangan = 0.20 * gaji_pokok
else:
    besar_tunjangan = 0

# proses perhitungan upah lembur
# di atas 200 jam di hitung lembur

if jam_kerja >= 200:
    upah_lembur = int(jam_kerja - 200) * Perjam_lembur
else:
    upah_lembur = 0

# Hitung pajak 10% sebagai persentase dari gaji pokok
total_gaji = gaji_pokok + besar_tunjangan + upah_lembur
potongan_pajak = total_gaji * pajak
gaji_bersih = total_gaji - potongan_pajak

# output
print("=======================================================================================")
print("nama karyawan        ", nama_karyawan)
print("gaji pokok          Rp ", int(gaji_pokok))
print("jumlah jam lembur       ", int(jam_kerja))
print("                         __________________ +")
print("gaji bersih         Rp ", int(gaji_bersih))
print("=======================================================================================")