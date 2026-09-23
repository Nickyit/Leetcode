class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n=len(nums)
        o_idx, e_idx = 0,1
        ans=[0]*n

        for num in nums:
            if num%2==0:
                ans[o_idx]=num
                o_idx+=2
            else:
                ans[e_idx]=num
                e_idx+=2


        return ans