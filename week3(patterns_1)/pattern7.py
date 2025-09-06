for i in range(1,6):
    for j in range(1,6-i):
        print("_",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()