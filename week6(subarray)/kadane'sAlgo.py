N=int(input())
L=list(map(int,input().split()))
cursum=L[0]
maxsum=L[0]
for i in range(N):
    cursum+=L[i]
    if(cursum>maxsum):
        maxsum=cursum
    elif(cursum<0):
        cursum=0
print(maxsum)