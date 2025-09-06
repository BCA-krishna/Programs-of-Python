for i in range(1,6):
    for j in range(2):
        if(i<=2 or i>3) or ( i==3 and j==1):
            print("*",end="")
        else:
            print("",end="")
    print()
