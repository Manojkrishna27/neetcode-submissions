class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        dummy=[]
        for i in range(len(word1)+len(word2)):
            if i<len(word1):
                dummy.append(word1[i])
            if i<len(word2):
                dummy.append(word2[i])
        return "".join(dummy)