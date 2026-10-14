class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        temp_arr= []
        
        for i in range(left,right+1):
            num=i
            self_div=True
            while(num>0):
                digit=num%10
                if digit == 0 or i % digit != 0:
                    self_div=False
                    break
                num//=10
            if self_div:
                temp_arr.append(i)

        return temp_arr