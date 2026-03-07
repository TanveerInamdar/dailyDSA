class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        result = []
        for i in range(len(nums1)):
            if nums1[i] not in hashmap:
                hashmap[nums1[i]] = 1
        for j in range(len(nums2)):
            if nums2[j] in hashmap:
                result.append(nums2[j])
                hashmap.pop(nums2[j])

        return result
