a = input()
count = 0
for i in range(len(a) - 2):  
    if a[i:i+3] == "bob":
        count += 1
print(count)
