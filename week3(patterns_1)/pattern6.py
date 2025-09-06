for i in range(1,6):
    for j in range(i,8):
        if(j==i or j==7):
            print("*",end="")
        else:
            print("_",end="")

        
    print()