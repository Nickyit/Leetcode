class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ=0
        pro=1
        while n!=0:
            rem = n%10
            summ+=rem
            pro*=rem
            n//=10

        ans = pro-summ
        return ans