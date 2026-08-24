class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r  # initialize result to the maximum possible rate

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
               hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
            # TODO: Calculate total hours needed to eat all piles at rate k
            # for each pile, add ceil(pile / k) to totalTime

            # TODO: Decide which half to search next
            # if totalTime <= h: this k works, save it and try smaller
            # else: this k doesn't work, try bigger

        return res