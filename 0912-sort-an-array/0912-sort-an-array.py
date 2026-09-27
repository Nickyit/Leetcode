class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums)<=1:
            return nums

        mid = len(nums)//2
        l=self.sortArray(nums[:mid])
        r=self.sortArray(nums[mid:])

        return self.merge(l,r)

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        sorted_arr = []
        i,j=0,0

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i+=1
            else:
                sorted_arr.append(right[j])
                j+=1        

        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])       
        return sorted_arr 