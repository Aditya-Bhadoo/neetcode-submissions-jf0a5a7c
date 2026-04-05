class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        loutputs=[]
        left=1
        for i in range(len(nums)):
            left*=nums[i]
            loutputs.append(left)
        
        right=1
        routputs=[]
        for i in range(len(nums)-1,-1,-1):
            right*=nums[i]
            routputs.append(right)
        routputs.reverse()
        outputs=[]
        for i in range(len(nums)):
            outputs.append((loutputs[i-1] if (i-1)>-1 else 1)*(routputs[i+1] if (i+1) < len(nums) else 1))
        return outputs

