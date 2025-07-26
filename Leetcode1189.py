class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashset = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for i in range(len(text)):
            if text[i] in hashset:
                hashset[text[i]] += 1
        hashset['l'] //= 2
        hashset['o'] //= 2
        return min(hashset.values())


