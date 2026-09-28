class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        dup = False
        for num in nums:
            seen[num] = seen.get(num,0)+1
    
        for key, val in seen.items():
            if val >=2:
                dup = True
                
        return dup