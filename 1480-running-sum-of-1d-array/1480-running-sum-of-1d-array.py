class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        new = []
        for num in nums:
            total += num
            new.append(total)
        
        return new