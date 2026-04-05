class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        
        l=0
        r=n-1
        
        while l<r:
            cur_sum=numbers[l]+numbers[r]
            if cur_sum == target:
                return [l+1,r+1]
            elif cur_sum > target:
                r-=1
                continue
            elif cur_sum < target:
                l+=1
                continue