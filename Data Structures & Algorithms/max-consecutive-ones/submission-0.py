class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one=0
        count=0
        for ch in nums:
            if ch ==1:
                one+=1
                count=max(count,one)
            else:
                one=0
        return count
                