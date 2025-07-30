class Solution:
    def isHappy(self, n: int) -> bool:
        has = {}
        x = n
        while x != 1:
            square = 0
            if x not in has:
                has[x] = 1
            else:
                return False
            for digit in str(x):
                square += int(digit) ** 2
            x = square
        return True