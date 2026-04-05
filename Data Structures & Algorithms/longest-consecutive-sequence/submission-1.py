class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count={}
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]]=1
            else:
                count[nums[i]]=1
        for i in range(len(nums)):
            if (nums[i]+1) in count:
                update(count,nums[i])
        return max(count.values())

def update(count,dig):
    if (dig+1) in count:
        count[(dig+1)]=count[dig]+1
        update(count,dig+1)
    else:
        return