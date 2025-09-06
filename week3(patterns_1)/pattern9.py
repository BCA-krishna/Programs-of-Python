
for i in range(1,6):
    for j in range(i,6):
        print("*",end=" ")
    for k in range(i*2-2):
        print(" ",end=" ")
    for l in range(i,6):
        print("*",end=" ")
    print()