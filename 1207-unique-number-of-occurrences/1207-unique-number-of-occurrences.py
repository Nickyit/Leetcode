class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dic= {}
        for i in arr:
            dic[i] = dic.get(i,0)+1

        return  len(dic) == len(set(dic.values()))