class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        listt =  [start + 2 * i for i in range(n)]
        a=0
        for i in listt:
            a^=i
        return a
        