class Solution:
    def reverseVowels(self, s: str) -> str:
        vovels = "aeiouAEIOU"
        listt = list(s)
        st = 0
        ed = len(listt)-1
        while st<ed:
            if listt[st] not in vovels:
                st+=1
            elif listt[ed] not in vovels:
                ed-=1
            else:
                listt[st],listt[ed] = listt[ed],listt[st]
                st+=1
                ed-=1
        return "".join(listt)


