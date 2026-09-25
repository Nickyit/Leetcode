class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l_idx=0
        r_idx= len(s)-1

        while l_idx < r_idx:
            s[l_idx],s[r_idx]=s[r_idx],s[l_idx]
            r_idx-=1
            l_idx+=1

        return s