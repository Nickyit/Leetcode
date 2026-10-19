class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        listt = [i*i for i in nums]
        listt.sort()
        return listt