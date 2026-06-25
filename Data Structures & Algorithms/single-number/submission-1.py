class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num=0
        for ch in nums:
            num^=ch
        return num