sub1=int(input("enter the marks in sub1 out of 100-->"))
sub2=int(input("enter the marks in sub2 out of 100 -->"))
sub3=int(input("enter the marks in sub3 out of 100-->"))
total_mark=sub1+sub2+sub3
percentage=(total_mark/300)*100
if percentage >=80:
    print("Grade:A")
elif percentage >=70 and percentage < 80:
    print("Grade:B")
elif percentage >=60 and percentage < 70:
    print("Grade:C")
elif percentage >=40 and percentage < 60:
    print("Grade:D")
else:
    print("Grade:E")
print("total_mark:",total_mark)
print("percentage:",percentage)
