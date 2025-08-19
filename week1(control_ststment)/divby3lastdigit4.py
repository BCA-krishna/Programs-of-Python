n=int(input("enter the number"))
if(n%3==0 and n%10==4):
     print("  divisible by 3 and last digit is 4")
elif (n%3==0):
    print(" divisible by 3 but last digit is not 4 ")   
elif (n%10==4):
    print("last digit is 4 but not divisible by 3 ")

