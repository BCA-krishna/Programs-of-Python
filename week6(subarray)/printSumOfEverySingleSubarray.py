s=int(input())
l=list(map(int,input().split()))
for i in range(s):
    sum=0
    for j in range(i,s):
        sum+=l[j]
        print(sum)