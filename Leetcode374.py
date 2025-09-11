# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def Binary(lo, hi):
            mid = (lo+hi) //2
            x = guess(mid)
            if x == 0:
                return mid
            if x == -1:
                return Binary(lo, mid-1)
            if x == +1:
                return Binary(mid+1, hi)

        return Binary(0,n)
