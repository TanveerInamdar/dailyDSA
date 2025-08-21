class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        x = piles[0]
        adder = 0
        for i in range(len(piles)):
            adder += piles[i]
            if piles[i] > x:
                x = piles[i]

        mini = ceil(adder / h)

        while mini < x:
            mid = (mini + x) // 2
            total = 0
            for pile in piles:
                total += (pile + mid - 1) // mid
            if total <= h:
                x = mid
            else:
                mini = mid + 1
        return mini


