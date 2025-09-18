A=list(map(int,input().split()))
min=A[0]
max=A[0]
for i in  range(len(A)):
    if(A[i]>max):
        max=A[i]
    if(A[i]<min):
        min=A[i]
print(max,min)