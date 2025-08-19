n=int(input("enter the number"))
n1=n
rev=0
while(n>0):
    digit=n%10
    rev=(rev*10)+digit
    n=n//10
if(n1==rev):
    print("the number is palindrome")