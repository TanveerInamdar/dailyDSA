class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        count = nums[0]
        for i in range(len(nums)):
            temp += nums[i]
            if temp > count:
                count = temp
            if temp < 0:
                temp = 0
        return count

