n=int(input())
arr=list(map(int,input().split()))
L, R = map(int, input().split())
L-=1
R-=1
sumtotal=sum(arr[L:R+1])
print(sumtotal)