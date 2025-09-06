
# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i  in range(4):
#     for j in range(4-i):
#         print("*",end=" ")
#     print()





n = int(input())
arr = map(int, input().split())
arr2 = []
    
maxx=0
for i in arr:
    if arr[i]>maxx:
        maxx=arr[i]
    for j in arr:
        if maxx<arr[i]:
            arr2.append(arr[j])
        ans=arr.max()
print(ans)