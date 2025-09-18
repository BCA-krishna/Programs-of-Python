A=list(map(int,input().split()))
odd=[]
even=[]
for i in A:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
for i in even:
    print(i,end=" ")
print()
for i in odd:
    print(i,end=" ")
