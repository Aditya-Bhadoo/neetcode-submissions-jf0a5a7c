class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = {}
        max_len = 0
        start = 0
        for i in range(len(s)):
                # print(f"Adding {s[i]}")
            if s[i] in hs:#abcabcbb
                currlen = i - start
                max_len = max(max_len, currlen)
                new_start = hs[s[i]]
                for ii in range(new_start, start - 1, -1):
                    # print(f"removing {s[ii]}, index = {ii};{i}", hs)
                    hs.pop(s[ii])
                start = new_start+1
            hs[s[i]] = i
            # print(f"max = {max_len} | start = {start}")
        return max(max_len, (len(s)-start))
