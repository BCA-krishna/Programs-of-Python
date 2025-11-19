n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    ans=[]
    for j in range(i,n):
        print(l[i:j+1])  

