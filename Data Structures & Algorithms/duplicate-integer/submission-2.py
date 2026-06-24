class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num=set()
        for ch in nums:
            if ch in num:
                return True
            num.add(ch)
        return False