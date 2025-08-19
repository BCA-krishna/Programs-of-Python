a1=int(input("enter the  1st angle"))
a2=int(input("enter the  2nd angle"))
a3=int(input("enter the 3rd angle"))
if(a1!=0 and a2!=0 and a3!=0):
    if( (a1+a2+a3)==180):
        print("valid triangle")
    else:
        print("invalid")
else:
    print("enter valid angles")
    

