l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])
print(l3)