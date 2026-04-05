class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs=[]
        total=1
        for num in nums:
            total*=num
        for i,num in enumerate(nums):
            
            if num == 0:
                prod=1
                for x,dig in enumerate(nums):
                    if x !=i:
                        prod*=dig
                outputs.append(prod)
            else:
                outputs.append(int(total/num))
        return outputs