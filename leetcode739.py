class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        prev_day = 0
        for i in range(len(temperatures)):
            while stk != [] and temperatures[stk[-1]] < temperatures[i]:
                prev_day = stk.pop()
                res[prev_day] = i - prev_day
            stk.append(i)

        return res