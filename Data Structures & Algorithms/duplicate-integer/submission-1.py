class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        else:
            cnt={}
            for x in nums:
                if x not in cnt:
                    cnt[x]=1
                else:
                    return True
            return False