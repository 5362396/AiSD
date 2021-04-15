#wersja 1
def isPalindrome1(s): 
    return s == s[::-1] 
    
#wersja 2
def isPalindrome2(str): 
    for i in xrange(0, len(str)/2): 
        if str[i] != str[len(str)-i-1]: 
            return False
    return True

#wersja 3
def isPalindrome3(s): 
    rev = ''.join(reversed(s)) 
    if (s == rev): 
        return True
    return False

#wersja 4
x = "malayalam"
w = "" 
for i in x: 
    w = i + w 
if (x==w): 
    print("YES")
    
s = "kamilślimak"
ans = isPalindrome1(s) 
print(ans)