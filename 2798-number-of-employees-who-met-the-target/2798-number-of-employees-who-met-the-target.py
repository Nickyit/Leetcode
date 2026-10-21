class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count=0
        for hr in hours:
            if hr >= target:
                count+=1
        return count

        return sum(hr>=target for hr in hours)