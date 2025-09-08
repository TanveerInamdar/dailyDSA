class Solution:
    def myAtoi(self, s: str) -> int:
        start = 0
        count = 0
        h = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        x = 0
        # skip spaces first
        while x < len(s) and s[x] == " ":
            x += 1
            start += 1
        sign = 1
        if x < len(s) and s[x] in ["+", "-"]:
            if s[x] == "-":
                sign = -1
            x += 1
            start += 1
        for i in range(start, len(s)):

            if s[i] in h:
                count += 1
            else:
                break

        if count == 0:
            return 0

        s = s[start: start + count]

        num = 0
        power = 0
        for i in range(len(s) - 1, -1, -1):  # from rightmost digit
            num += h[s[i]] * (10 ** power)
            power += 1
        num = num * sign
        mi, ma = -2 ** 31, 2 ** 31 - 1
        if num < mi:
            return mi
        if num > ma:
            return ma
        return num
