class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_map={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in num_map:
                num_map[nums[i]]=set([i])
            else:
                num_map[nums[i]].add(i)
        ans=set()
        for a in range(n):
            for b in range(a+1,n):
                inv_sum = -(nums[a] + nums[b])
                if inv_sum in num_map:
                    for c in num_map[inv_sum]:
                        pos=tuple(sorted((nums[a],nums[b],nums[c])))
                        if c!=a and c!=b:
                            ans.add(pos)

        return [list(x) for x in ans]
