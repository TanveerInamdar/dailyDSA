class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        start = 0
        maxlen = 0
        for i in range(len(s)):
            if s[i] in hashmap and hashmap[s[i]] >= start:
                start = hashmap[s[i]] + 1

            hashmap[s[i]] = i
            if i - start + 1 > maxlen:
                maxlen = i - start + 1
        return maxlen