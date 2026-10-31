class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        idx = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[idx]:
                idx+=1
                nums[i],nums[idx]=nums[idx],nums[i]
        return idx+1

        # i =0
        # while i<len(nums)-1:
        #     if nums[i]==nums[i+1]:
        #         nums.pop(i+1)
        #     else:
        #         i+=1
        # return i+1