# arr=[3,-1,4]
# result=0

# for i in range(len(arr)):
#     sum=0
#     ea=[]
#     for j in range(i,len(arr)):
#         ea.append(arr[j])
        
#         # sum+=arr[j]
#         # result+=sum
        
#         print(ea)
# print(result)
#if we know how many subarray each element coming  we can solve it fast

# how many subarray index 3  is present 3-2 4 -1 2 6
        

# index=  0  1 2  3 4 5
# arr=    3 -2 4 -1 2 6
# start=[ 1 2 3  4 5 6 ]
# end=  [ 6 5 4  3 2 1 ]
# total=[6 10 12 12 10 6]
# sum=  [18 -20 48 -12 20 36]

# arr=[3,-2,4,-1,2,6]
# start=[ 1, 2 , 3, 4, 5, 6 ]
# end=[ 6, 5 ,4 , 3, 2, 1 ]
# result=0
# for i in range(len(arr)):
#     result+=arr[i]*start[i]*end[i]
# print(result)


# given an array A  of non negitive number  and  non negitive B
# find subarray sum less than B

# A=[2,5,6]
# B=10
# c=0
# for i in range(len(A)):
#     sum=0
#     for j in range(i,len(A)):
#         sum+=A[j]
#         if (sum<B):
#             c+=1
# print(c)


# given an array of int A is sum array of an array is said to be good if it fullfills anyone of the criteria 
# len is even and sum of all element of the subarray must be less than  b
# len is odd and sum of all element of the subarray must be greater than  b
# your task is to find count of good subarray in A

# A=[2,5,6]
# B=10
# c=0
# for i in range(len(A)):
#     sum=0
#     for j in range(i,len(A)):
#         if len(A)%2==0:
#             sum+=A[j]
#             if (sum<B):
#                 c+=1
#         else:
#             sum+=A[j]
#             if (sum>B):
#                 c+=1
        
# print(c)



# you  have gien  integer an array of size a now u need to find  a subarry so that the sum of continous element is maximum but 
# sum must not exceed B
# A=5
# B=12
# c=[2,1,3,4,5]
# maxsum=0
# for i in range(len(c)):
#     sum=0
#     for j in range(i,len(c)):
#         sum+=c[j]
#         if sum>B:
#             break
#         if(maxsum< sum):
#             maxsum=sum

# print(maxsum)


# given an array a length your task is to find maximum possible sum 
# of any non empty contigious subarray in other words among all possible subaary of
# a determine the one that yeilds the highest sum and return the sum

A= [-2 ,1, -3, 4 ,-1 ,2 ,1, -5 ,4]
max=0
cursum=0
for i in range(len(A)):
    cursum+=A[i]
    if cursum<0:
        cursum=0
    if max<cursum:
        max=cursum
print(max)

# s=input()
# ans=[]
# for i in range(len(s)):
#     c=s.count(s[i])
#     if(s[i] not in ans):
#         ans.append(s[i])
#         if(c>1):
#             ans.append(str(c))

# res=''.join(ans)
# print(res)

# from collections import Counter
# s = input()
# freq = Counter(s)
# print(freq)








