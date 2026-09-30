class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        result = sorted(nums,reverse=True)
        return result[k-1]