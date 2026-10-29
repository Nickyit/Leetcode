class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        summ = 0
        max_sum = 0
        for i in accounts:
            summ=sum(i)
            max_sum=max(summ,max_sum)
        return max_sum