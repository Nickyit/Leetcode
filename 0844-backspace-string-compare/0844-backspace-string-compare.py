class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1=[]
        st2=[]

        for word in s:
            if word == '#':
                if st1:
                    st1.pop()
            else:
                st1.append(word)
        for word in t:
            if word == '#':
                if st2:
                    st2.pop()
            else:
                st2.append(word)
        
        return st1 == st2
        
        