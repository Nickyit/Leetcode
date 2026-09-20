class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            rem = 0
            while num > 0:
                rem += num % 10
                num = num // 10
            num = rem  
        return num