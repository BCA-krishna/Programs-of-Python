n=int(input("enter the number"))
if(n%7==0 or n%10==5):
    if(n%7==0 and n%10==5):
        print("it is divisible by 7 and last digit is also 5")
    elif(n%7==0):
        print("divisible by 7 but last digit is not 5")
    elif(n%10==5):
        print("last digit is 5 but not divisible by 7")
else:
    print("not divisible by 7 and last digit is not 5")