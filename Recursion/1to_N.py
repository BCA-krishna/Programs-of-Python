def oneTO_n(n):
    if n == 0:       
        return
    oneTO_n(n - 1)  
    print(n, end=" ")     
n = int(input())
oneTO_n(n)
