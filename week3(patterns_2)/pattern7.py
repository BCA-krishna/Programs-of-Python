
for i in range(1,6):
    for j in range(5):
        if(i==1 or i==5) or ( j>2):
            print("*",end="")
        else:
            print("",end="")
    print()
