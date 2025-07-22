class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        num = {}

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if nums[i] in num:
                    num[nums[i]] += 1
                else:
                    num[nums[i]] = 1
        if num != {}:
            high = max(num.values())
        else:
            return -1
        return min(k for k, v in num.items() if v == high)

