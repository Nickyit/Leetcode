class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        all_xor = 0
        for i in nums:
            all_xor^=i

        mask = all_xor & -all_xor

        n1=0
        n2=0
        for i in nums:
            if mask & i:
                n1^=i
            else:
                n2^=i
        return n1,n2