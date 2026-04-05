class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums).most_common(k)
        ans=[]
        for i in cnt:
            ans.append(i[0])
        return ans