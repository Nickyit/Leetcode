class Solution:
    def merge(self, arr1: list[int], m: int, arr2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n=len(arr1)-len(arr2)
        m=len(arr2)
        i=n-1
        j=m-1
        idx=n+m-1
        while(i>=0 and j>=0):
            if arr1[i]>=arr2[j]:
                arr1[idx]=arr1[i]
                idx-=1
                i-=1
            else:
                arr1[idx]= arr2[j]
                idx-=1
                j-=1

        while j>=0:
            arr1[idx]=arr2[j]
            idx-=1
            j-=1