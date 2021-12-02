string = input("Masukan kata : ")
print("Output :", end="")
length = len(string)
for i in range(0, length, 1):
    for j in range(0, i , 1):
        print(string[j], end='')
    print()
for i in range(length, 0, -1):
    for j in range(0, i):
        print(string[j], end='')
    print()