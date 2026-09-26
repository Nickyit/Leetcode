class Solution:
    def missingNumber(self, nums: list[int]) -> int: 
        n=len(nums)
        # Check every number from 0 to n
        for i in range(n + 1):
            found = False
            # Search for 'i' in the array
            for num in nums:
                if num == i:
                    found = True
                    break
            
            # If 'i' was never found, it's the missing number
            if not found:
                return i
                
        return -1

