# A=input()
# A=A+A
# vowel="aeiou"
# res=""
# for i in A:
#     if i.isupper():
#         continue
#     else:
#         if i in vowel:
#             res+="#"
#         else:
#             res+=i
# print(res)
str1="aaabbccds"
n=len(str1)
count=0
ans=[]
for i in range(0,n):
    if(str1[i]==str1[i-1]):
        count=str1.count(str1[i])
        ans.append(str1[i])
        ans.append(count)
    else:
        count=0
        # ans.append(str1[i])
print(ans)

