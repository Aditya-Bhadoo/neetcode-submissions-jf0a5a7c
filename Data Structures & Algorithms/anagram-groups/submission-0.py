class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap={}
        for i in range(len(strs)):
            amap[i]=Counter(strs[i])
        # print(amap)
        
        if len(amap)>0:
            buckets = [[(0,strs[0])]]
            for i in range(1,len(strs)):
                found_bucket = 0
                for buc in buckets:
                    if amap[i] == amap[buc[0][0]]:
                        buc.append((i,strs[i]))
                        found_bucket = 1
                        break
                if found_bucket == 0:
                    buckets.append([(i,strs[i])])
            # print(buckets)
            answer = []
            for buk in buckets:
                ll = []
                for tup in buk:
                    ll.append(tup[1])
                answer.append(ll)
            return answer
        else:
            return [[]]