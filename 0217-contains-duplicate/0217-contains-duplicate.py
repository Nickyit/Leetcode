class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        dup = False
        for num in nums:
            if num in seen:
                dup = True
                break
            seen.add(num)

        return dup