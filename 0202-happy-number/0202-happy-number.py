class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1 and n!=4:
            t_sum = 0
            while n>0:
                t_sum+=(n%10)**2
                n//=10
            n=t_sum
        return n==1