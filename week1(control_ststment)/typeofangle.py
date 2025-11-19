a1=int(input("enter the first angle"))
a2=int(input("enter the second angle"))
a3=int(input("enter the thord angle"))
if (a1+a2+a3)!=180:
    print("invalid angles")
elif(a1==90 or a2==90 or a3==90):
    print("right angle")
elif (a1>90 or a2> 90 or a3>90):
    print("obtuse angle")
else:
    print("acute angle")

