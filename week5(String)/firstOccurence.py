A = input()
B = int(input())
ch = chr(B)  

if ch in A:
    print(A.find(ch))
else:
    print(-1)
