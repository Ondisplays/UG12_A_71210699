orang = []
duduk = []
x = 0

while (x < 1):
    nama = input("Masukkan nama: ")
    if nama == "STOP":
        break
    kursi = int(input("Masukkan nomor kursi {} : " .format(nama)))
    if kursi in duduk:
        print("Mohon maaf kursi tersebut telah terisi!")

    if kursi not in duduk:
        orang.append(nama)
        duduk.append(kursi)
print()
print("List kursi yang telah terisi : ")
for a in range(0, len(duduk), 1):
    print("Kursi nomor", duduk[a], "telah diisi oleh", orang[a])