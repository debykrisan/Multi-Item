'''
Deby Krisan Anggraeni 
'''
print("==============================================")
print(" CAFFE KRISAN ")
print("==============================================")
print("Menu Makanan")
print("a. Nasi Goreng                 15.000")
print("b. French Fries                14.500")
print("c. Bakso Goreng                11.900")
print("d. Rujak Cireng                10.500")
print("e. Siomay Goreng               12.000")
print("f. Spagethi                    20.000")
print("==============================================")
print("Menu Minuman")
print("a. Lemon Tea                 15.000")
print("b. MilkShake                 20.000")
print("c. Thai Tea                  10.000")
print("d. Matcha                    15.900")
print("e. Red Velvet                15.000")
print("==============================================")
print(" ")

#1. Menyiapkan Variabel
kode=['a','b','c','d','e','f','g','h','i','j','k']
namaMakanan_Minuman=['Nasi Goreng','French Fries','Bakso Goreng','Rujak Cireng','Siomay Goreng','Spagethi',
            'Lemon Tea','MilkShake','Thai Tea','Matcha','Red Velvet']
harga=['15000','14500','11900','10500','12000','20000',
        '15000','20000','10000','15900','15000']

#2.Input Barang
pilihan = input(">> Masukkan Kode Makanan atau minuman    = ")
#3. INPUT QTY
qty     = input(">> Masukkan Jumlah Pesanan  = ")
 
    

#4. HITUNG BAYAR
##cek nama barang dan ambil harga satuan
i = 0
while i<len(namaMakanan_Minuman):
        #jika value pada list kode[i] == pilihan
            if kode[i] == pilihan:
            #ambil nama barang
                nm_brg = namaMakanan_Minuman[i]

            #ambil harga satuan
                hrg_sat = harga[i]
            
        #jika tidak cocok, lanjut ke i berikutnya
                i+=1
            
            
            tot_byr = int(hrg_sat) * int(qty)
        

        #5. TAMPILKAN 
print(">>> NAMA BARANG      : " + nm_brg)
print(">>> HARGA BARANG     : Rp." + str(hrg_sat))
print(">>> JUMLAH BARANG    : " + qty)
print(("-------------------------------"))
print(">>> TOTAL BAYAR      : Rp." + str(tot_byr))
uang = input(">>> UANG             : Rp.")
x = int(uang)
kembalian = x - tot_byr
print("Kembalian            : Rp."+ str(kembalian))
