angka = input("Masukkan deret angka : ")
split = angka.split(",")
count = len(split)

if(int(split[0]) % 2 == 0):
    awal = split[0]
    sum = int(awal)
else:
    awal = int(split[0])*-1
    sum = int(awal)

print("Total :",awal,end="")

for jumlah in split[1:count]:
    if(jumlah != split[0]):
        if (int(jumlah) % 2 == 1):        
            jumlah = int(jumlah) * -1
            sum = sum + int(jumlah) 
            print("",jumlah,end="")
        elif(int(jumlah) % 2 == 0):
            sum = sum + int(jumlah) 
            if (jumlah == split[0]):
                print(jumlah,end="")
            else:
                print(" +",jumlah,end="")
    
print()
print("Hasil perhitungan diatas ialah",sum)
