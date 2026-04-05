class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnts = {}
        for x in s:
            if x not in cnts:
                cnts[x]=1
            else:
                cnts[x] = cnts[x]+1

        cntt={}
        for x in t:
            if x not in cntt:
                cntt[x]=1
            else:
                cntt[x] = cntt[x]+1
        return cnts == cntt

