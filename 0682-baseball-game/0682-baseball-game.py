class Solution:
    def calPoints(self, operations: list[str]) -> int:
        neww=[]
        for op in operations:
            if op == '+':
                n_val = neww[-1]+neww[-2]
                neww.append(n_val)
            elif op=='D':
                n_val  = neww[-1]*2
                neww.append(n_val)
            elif op=='C':
                neww.pop()
            else:
                neww.append(int(op))
        return sum(neww)
