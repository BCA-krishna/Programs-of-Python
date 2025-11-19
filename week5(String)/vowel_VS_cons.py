
T=int(input("how many words: "))

vowels=['a','e','i','o','u','A','E','I','O','U']
vl=[]
cl=[]
for i in range(T):
    s=input("enter the word: ")
    v=0
    c=0
    for i in s:
        if i in vowels:
            v += 1
        elif i != ' ':
            c += 1
    vl.append(v)
    cl.append(c)

for i in range(T):
    print(vl[i], cl[i])
