a1=int(input("enter the number"))
if(a1<90):
    print("acute angle")
elif(a1==90):
    print("right angle")
elif(a1>90 and a1<180):
    print("straight angle")
elif(a1>180 and a1<360):
    print("reflex angle")
elif(a1==360):
    print("complete angle")
else:
    print("invalid input")

