class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maxCount=0
        for sent in sentences:
            count=0
            for word in sent.split():
                count +=1
            maxCount=max(count,maxCount)
        return maxCount