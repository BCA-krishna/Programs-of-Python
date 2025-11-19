def is_palindrome(s, start, end):
    if start >= end: 
        return True
    if s[start] != s[end]:  
        return False
    return is_palindrome(s, start + 1, end - 1)  
s = input()
if is_palindrome(s, 0, len(s) - 1):
    print("Palindrome")
else:
    print("Not Palindrome")
