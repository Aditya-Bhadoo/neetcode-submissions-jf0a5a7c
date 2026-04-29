class Solution:
    def maxProfit(self, pr: List[int]) -> int:
        minp=1000
        maxprof=-1
        for i in range(len(pr)):
            maxprof=max(maxprof,pr[i]-minp)
            minp=min(pr[i],minp)
        return max(maxprof,0)
