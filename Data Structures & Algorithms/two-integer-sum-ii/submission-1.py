class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        
        l=0
        r=n-1
        
        while r>=0 and l<n:
            left=numbers[l]
            right=numbers[r]
            print(left,right)
            
            if left+right == target:
                return [l+1,r+1]
            elif left+right > target:
                r-=1
                continue
            elif left+right < target:
                l+=1
                continue