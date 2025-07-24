class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        count = 0
        prev = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                count += accounts[i][j]
            if count> prev:
                prev = count
            count = 0
        return prev