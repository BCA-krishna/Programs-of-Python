percentage=float(input("enter the percentage"))
if(percentage>85):
    print("GRADE-A+")
elif(percentage<=85 and percentage>65):
    print("GRADE-A")
elif(percentage<65 and percentage>=45):
    print("GRADE-B")
elif( percentage<45 and percentage>=25):
    print("GRADE-C")
else:
    print("GRADE-D")