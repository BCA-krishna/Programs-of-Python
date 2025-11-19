def n_to_1(n):
    if n == 0:      
        return
    print(n, end=" ")    
    n_to_1(n - 1)   
n = int(input())
n_to_1(n)
