n1=int(input("enter the number 1st"))
n2=int(input("enter the number 2nd"))
n3=int(input("enter the number 3rd"))
if(n1<n2 & n1<n3):
    print(n1,"is minimum")
elif(n2<n1 & n2<n3):
    print(n2,"is minimum")
else:
    print(n3,"is minimum")
