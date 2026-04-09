class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l=0
        r=n-1
        maxi=0
        while(l<r):
            left=heights[l]
            right=heights[r]
            maxi=max(maxi,min(left,right)*(r-l))
            if left<=right:
                l+=1
            else:
                r-=1
        return maxi
