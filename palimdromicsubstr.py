


s = "  bdyzzydbdyzydx"
c = 0

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if s[i:j]==s[j:i:-1]: 
            l=j-i+1
            if l>c:
                c = l
print(c)

# given a number N index i print ith bit of 10
# output=1
