# Nama Program : Gofood

# ALGORITMA

jarak = float(input("Nilai jarak: "))
if (jarak > 40):
    quit("Terlalu Jauh")

# Makanan
ar_makan = ["Sushi", "Caviar"]
ar_harga = [15000, 40000]
cart_makan = []
cart_harga = []
for i in range (0, len(ar_makan)):
    print(f"{i}. {ar_makan[i]}: Rp {ar_harga[i]},00")
ulang = True
while ulang:
    print(cart_makan)
    print(cart_harga)
    inputmakan = int(input("Masukkan Nomor Makanan : "))
    inputjumlah = int(input("Masukkan Jumlah Makanan : "))
    if (inputmakan == 666):
        ulang = False
    else:
        for i in range(inputjumlah):
            cart_makan.append(ar_makan[inputmakan])
            cart_harga.append(ar_harga[inputmakan])

print(cart_makan)
print(cart_harga)

hargamakan = 0

for i in range (0, len(cart_makan)):
    hargamakan += cart_harga[i]

# Ongkir
# (0km - 5km) = 4000
# After that, every 2km = +2000
if (jarak <= 5):
    ongkir = 4000
else:
    jarak2 = jarak-5
    kali = (jarak2//2) + 1
    ongkir = 4000 + kali*2000

# Biaya Jasa
# Base = 10000
# Jika kuantitas makanan > 20, jasa +10000/5
if(len(cart_makan) > 20):
    countjasa = (len(cart_makan)-20)//5 + 1
    jasa = 10000 + countjasa*10000
else:
    jasa = 10000

total = hargamakan + ongkir + jasa

print(f"Maka, harga total yang harus dibayar adalah : Rp. {total}")