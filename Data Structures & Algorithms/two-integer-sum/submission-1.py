import bisect
#[1,3,4,5,6] 8

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            map[nums[i]]=i
        for i in range(len(nums)):
            if target - nums[i] in map and map[target - nums[i]] != i:
                return sorted([i,map[(target - nums[i])]])