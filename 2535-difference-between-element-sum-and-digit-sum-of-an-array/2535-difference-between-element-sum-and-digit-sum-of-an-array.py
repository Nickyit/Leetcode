class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        arr_sum = sum(nums)
        d_sum=0
        for num in nums:
            while num>0:
                rem = num%10
                d_sum += rem
                num//=10
        return arr_sum-d_sum