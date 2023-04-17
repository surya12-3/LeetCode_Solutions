class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        res = [True for i in range(len(candies))]

        for i in range(0,len(candies)):
            if candies[i] + extraCandies < mx:
                res[i] = False
        return res        
