A=list(map(int,input().split()))
n=len(A)
for i in range(0,n//2):
    A[i],A[n-i-1]=A[n-i-1],A[i]
print(A)
