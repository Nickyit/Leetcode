class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        k = s[0]
        count = 0
        for ch in s:
            if ch != k:
                count+=1
                k=ch
            
        return count