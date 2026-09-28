class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s)!=len(t):
            return False
        for ch in s:
            seen[ch]=seen.get(ch,0)+1
        for ch in t:
            seen[ch]=seen.get(ch,0)-1

        for key,val in seen.items():
            if val != 0:
                return False
        return True