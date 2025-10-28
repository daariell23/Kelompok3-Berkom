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
Jika ingin menambah pesanan ketik     : 1
Jika ingin mengurangi pesanan ketik   : 2
    """)

print("=== Selamat datang di aplikasi pemesanan Online === \n")
jarak = float(input("Berapa jarak rumah anda dengan restoran? : "))
if (jarak > 40):
    quit("Jarak rumah anda terlalu jauh, tidak bisa melakukan pemesanan")

# Makanan
print("\n=== Silahkan pilih menu yang ingin dipesan === \n")
ar_makan = ["Salmon Maki", "Crunchy Salmon Roll", "Tamago Sushi", "Kani Mentai Mayo Roll", "Tuna Maki", "Gyudon", "Chicken Katsu Curry Rice", "Salmon Teriyaki Don"]
ar_harga = [40000, 80000, 35000, 70000, 50000, 70000, 70000, 90000]
for i in range (0, len(ar_makan)):
    print(f"{i+1}. {ar_makan[i]} : Rp {ar_harga[i]},00")
print("\n")

pemesanan_makanan()
lanjut = int(input("Ingin tambah pesanan atau mengurangi? : "))

while lanjut == 1 :
    pemesanan_makanan()
    lanjut = int(input("Ingin tambah pesanan atau mengurangi? : "))

while lanjut == 2 :
    print(cart_makan)
    Hapus = int(input("Makanan mana yang ingin anda hapus? : "))
    del cart_makan[Hapus - 1]
    lanjut = int(input("Ingin tambah pesanan atau mengurangi? : "))

print(f""" 
Total makanan yang anda pesan 
Salmon Maki  = {cart_makan.count('Salmon Maki')} Pcs
Crunchy Salmon Roll = {cart_makan.count('Crunchy Salmon Roll')} Pcs
Tamago Sushi = {cart_makan.count('Tamago Sushi')} Pcs
Kani Mentai Mayo Roll = {cart_makan.count('Kani Mentai Mayo Roll')} Pcs
Tuna Maki = {cart_makan.count('Tuna Maki')} Pcs
Gyudon = {cart_makan.count('Gyudon')} Pcs
Chicken Katsu Curry Rice = {cart_makan.count('Chicken Katsu Curry Rice')} Pcs
Salmon Teriyaki Don = {cart_makan.count('Salmon Teriyaki Don')} Pcs
""")

#Harga makanan
Harga_salmon = cart_makan.count('Salmon Maki') * ar_harga[0]
Harga_Crunchy = cart_makan.count('Crunchy Salmon Roll') * ar_harga[1]
Harga_tamago = cart_makan.count('Tamago Sushi') * ar_harga[2]
Harga_Kani = cart_makan.count('Kani Mentai Mayo Roll') * ar_harga[3]
Harga_Tuna = cart_makan.count('Tuna Maki') * ar_harga[4]
Harga_Gyudon = cart_makan.count('Gyudon') * ar_harga[5]
Harga_chicken = cart_makan.count('Chicken Katsu Curry Rice') * ar_harga[6]
Harga_teriyaki = cart_makan.count('Salmon Teriyaki Don') * ar_harga[7]

Harga_makanan_total = Harga_salmon + Harga_Crunchy + Harga_tamago + Harga_Kani + Harga_Tuna + Harga_Gyudon + Harga_chicken + Harga_teriyaki

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

total = Harga_makanan_total + ongkir + jasa

print(f"\nMaka, harga total yang harus dibayar adalah : Rp. {total:.0f},00")