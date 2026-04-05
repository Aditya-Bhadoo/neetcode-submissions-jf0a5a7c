class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest_sequence=0
        for dig in num_set:
            if dig-1 not in num_set:
                ccnt=1
                while (dig+1) in num_set:
                    ccnt+=1
                    dig+=1
                longest_sequence=max(longest_sequence,ccnt)
        return longest_sequence