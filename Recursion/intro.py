# it is the programming techinique in which the function call directly or indirectly in order to solve the problem
# in Recursion function one or more solve itself as a part of execution
# in a recursive function the function makes one or more call to itself as a part of its execution.
# the process continue until a base case is reached at wich point the function stop calling itself and returns a result.


# make an assumption
# decide what your function does and trust that it will do 
# main logic
# solve the bigger problem using subprob
# base case
# when the recurion stop

# sum of an natural number:
# n=int(input())
# sum=0
# for i in range(1,n):
#     sum+=i
# sum
# print(sum)

# def sum(n):
#     if(n==1):
#         return 1
#     return(sum(n-1)+n)
# n=int(input("enter n :"))
# print(sum(n))

# calc factorial with recursion
# def fact(n):
#     f=1
#     if(n==0):
#         return 1
#     return(fact(n-1)*n)


# n=int(input(" enter n "))
# print(fact(n))

# wap to print 1 to n using recursion


# def numbers(n):
#     if n == 0:
#         return  
#     numbers(n - 1) 
#     print(n)  


# n = int(input("enter the number : "))
# numbers(n)

# nto 1

# def numbers(n):
#     if n == 0:
#         return 
#     print(n)   
#     numbers(n - 1) 
    



# n = int(input("enter the number : "))
# numbers(n)

# using a recursion function find the Nth  fibonacci number

# def fib(n):
    
#     if(n<=1):
#         return n
    
#     return fib(n-1) + fib(n-2)
# n=int(input(" enter num"))
# for i in range(n):
#     print(fib(n),end=" ") 


# # find the sum of digit using recursion 
# def sumdigit():
#     if(n==0):
#         return 0
    
# n=int(input("enter number"))





# reverse a string using Recursion




# binary search using recuirsion

# n=int(input())
# arr=list(map(int,input().split()))
# tar=int(input("target"))
# l=0
# h=len(arr)-1
# while(l<=n):
#     mid=(l+h)/2

# def binary_search(arr, low, high, key):
#     if low > high:
#         return -1  # not found

#     mid = (low + high) // 2

#     if arr[mid] == key:
#         return mid
#     elif arr[mid] > key:
#         return binary_search(arr, low, mid - 1, key)
#     else:
#         return binary_search(arr, mid + 1, high, key)

# # Input
# n = int(input("Enter number of elements: "))
# arr = sorted([int(input()) for _ in range(n)])  # sorted list is required
# key = int(input("Enter element to search: "))

# # Call function
# result = binary_search(arr, 0, n - 1, key)

# # Output
# if result != -1:
#     print("Element found at index", result)
# else:
#     print("Element not found")


# given an array elemnts ,every elemnt  repeate twice except 1 find the unique
# a=[6,7,9,7,6]
# c=0
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if(a[i]==a[j]):
#             a[i]=-1
#             a[j]=-1
# print(max(a))

            #ORRRRRRRRRRRRRRRRRRRRR#
        
# for i in range(len(a)):
#     c=a.count(a[i])
#     if(c==1):
#         print(a[i]) 

# def singlenum(arr):
#     ans=0
#     n=len(arr)
#     for i in range(n):
#         ans=ans^arr[i]
#     return ans
# arr=[6,7,9,7,6]
# print(singlenum(arr))

# n=21
# b=2
# if((n>>b )& 1):
#     print("set")
# else:
#     print("unset")


#given an interger n  count how many set bit are there in n
# n=13
# c=0
# while n > 0:
#     if(n & 1)==1:
#         c=c+1
#     n=n>>1
# print(c)


#  give an arr of n integer where all numbrs occure even no of  time except one
# first line of input contains integer n demoting sixe of the Arr
# next line of input containg a seprated onteger denoting element if array

# a=[2,2,3,3,2,2,4]
# ans=0
# for i in a:
#     ans=ans^i
# print(ans)














































































































































































































































































































