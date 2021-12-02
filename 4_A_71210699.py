z = int(input("Input : "))
gg = 2
for x in range (1,z+1):
    for y in range (1,2*z) :
        if x+y==z+1 or y-x==z-1:
            print ("*", end="")
        elif x==z and y!= gg:
            print ("*",end="")
            gg = gg + 2
        else:
            print (end=" ")
    print ()