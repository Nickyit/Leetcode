class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        c_sum =nums[0]
        for i in range(1,len(nums)):
            c_sum=max(c_sum+nums[i],nums[i])
            max_sum = max(max_sum, c_sum)
        return max_sum