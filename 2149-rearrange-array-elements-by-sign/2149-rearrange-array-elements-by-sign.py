class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        p_idx, n_idx = 0,1
        ans=[0]*n

        for num in nums:
            if num>0:
                ans[p_idx]=num
                p_idx+=2
            else:
                ans[n_idx]=num
                n_idx+=2


        return ans