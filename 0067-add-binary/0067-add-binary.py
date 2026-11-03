class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        # Loop as long as there are digits to process or a carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # The bit to append is total % 2 (either 0 or 1)
            res.append(str(total % 2))
            # The new carry is total // 2 (either 0 or 1)
            carry = total // 2
            
        # The result is built backwards, so reverse it at the end
        return "".join(reversed(res))
