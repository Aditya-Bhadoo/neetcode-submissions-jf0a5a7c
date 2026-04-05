class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest_sequence=0
        for dig in num_set:
            if dig-1 not in num_set:
                new=update(num_set,dig,1)
                print(new)
                longest_sequence=max(longest_sequence,new)
        return longest_sequence
    
def update(num_set,dig,cnt):
    if dig+1 in num_set:
        return update(num_set,dig+1,cnt+1)
    else:
        return cnt
