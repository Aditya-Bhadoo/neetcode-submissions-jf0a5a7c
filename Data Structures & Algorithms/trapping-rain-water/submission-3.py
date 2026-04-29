class Solution:
    def trap(self, ht: List[int]) -> int:
        # start from the beginning and look for anything above 0
        # when you get a hit, do this until you get something higher(this will be the next hit) than that hit
        # calculate the difference between that height and the hit
        lmax=[0 for _ in range(len(ht))]
        rmax=[0 for _ in range(len(ht))]

        lcur=0
        for l in range(len(ht)):
            lcur = max(ht[l],lcur)
            lmax[l]=lcur
        hcur=0
        for r in range(len(ht)-1,-1,-1):
            hcur=max(ht[r],hcur)
            rmax[r] = hcur
        twater=0
        for i in range(len(ht)):
            water=min(lmax[i],rmax[i])-ht[i]
            if water < 0:
                continue
            twater+=water

        return twater