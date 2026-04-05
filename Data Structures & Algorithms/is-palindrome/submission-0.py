class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lrev=list(s)[::-1]
        # rev="".join(lrev)
        # print(type(rev),rev.lower())
        # if rev.lower()==s.lower():
        #     return True
        # else:
        #     return False
        
        s=cleanup(list(s))
        revs=cleanup(list(s)[::-1])
        if s==revs:
            return True
        else:
            return False

def cleanup(lstr):
    cleanl=[]
    for s in lstr:
        if s.isalnum():
            cleanl.append(s.lower())
    return "".join(cleanl)