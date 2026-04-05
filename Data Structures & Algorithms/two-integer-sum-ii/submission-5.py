class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        
        l=0
        r=n-1
        
        while r>=0 and l<n:
            
            if numbers[l]+numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r] > target:
                r-=1
                continue
            elif numbers[l]+numbers[r] < target:
                l+=1
                continue