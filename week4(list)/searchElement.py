A=list(map(int,input().split()))
B=int(input("enter search"))
for i in range(len(A)):
    if(A[i]==B):
        print(i)
        break
