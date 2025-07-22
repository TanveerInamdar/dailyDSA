class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [0] * (len(nums))
        r = [0] * (len(nums))
        l[0] = 1
        r[len(nums) - 1] = 1
        l[1] = nums[0]
        r[len(nums) - 2] = nums[len(nums) - 1]
        for i in range(2, len(nums)):
            l[i] = l[i - 1] * nums[i - 1]

        for i in range(len(nums) - 3, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]

        arr = []
        for i in range(0, len(nums)):
            arr.append((l[i] * r[i]))
        return arr



