# Nama Program : Gofood

#inisiasi

cart_makan = []
cart_harga = []
hargamakan = 0

# ALGORITMA

def pemesanan_makanan() :
    inputmakan = int(input("Silahkan pilih nomor menu yang tersedia : ")) - 1
    inputjumlah = int(input("Berapa banyak yang ingin dipesan? : "))

    for i in range(inputjumlah):
        cart_makan.append(ar_makan[inputmakan])
        cart_harga.append(ar_harga[inputmakan])
    print(cart_makan)
    print(cart_harga)

    print(""" 
Apakah masih ingin menambah pesanan?
jika iya ketik   : 1
    """)

print("=== Selamat datang di aplikasi pemesanan Online === \n")
jarak = float(input("Berapa jarak rumah anda dengan restoran? : "))
if (jarak > 40):
    quit("Jarak rumah anda terlalu jauh, tidak bisa melakukan pemesanan")

# Makanan
print("\n=== Silahkan pilih menu yang ingin dipesan === \n")
ar_makan = ["Sushi", "Caviar"]
ar_harga = [15000, 40000]
for i in range (0, len(ar_makan)):
    print(f"{i+1}. {ar_makan[i]} : Rp {ar_harga[i]},00")
print("\n")

pemesanan_makanan()
lanjut = int(input("Ingin tambah pesanan? : "))

if lanjut == 1 :
    pemesanan_makanan()
    lanjut = int(input("Ingin tambah pesanan? : "))

print(f""" 
Total makanan yang anda pesan 
Sushi  = {cart_makan.count('Sushi')} Pcs
Caviar = {cart_makan.count('Caviar')} Pcs
""")


for i in range (0, len(cart_makan)):
    hargamakan += cart_harga[i]

# Ongkir
# (0km - 5km) = 4000
# After that, every 2km = +2000
if (jarak <= 5):
    ongkir = 4000
else:
    jarak2 = jarak-5
    kali = -(-jarak2//2)
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

print(f"\nMaka, harga total yang harus dibayar adalah : Rp. {total:.0f},00")