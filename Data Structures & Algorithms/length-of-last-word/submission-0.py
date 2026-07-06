class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s[::-1]
        s=s.strip()
        count=0
        for ch in s:
            if ch!=" ":
                count+=1
            if ch==" ":
                break
        return count