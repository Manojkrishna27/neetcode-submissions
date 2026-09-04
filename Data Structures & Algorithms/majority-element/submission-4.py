class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)

        freq={}
        for ch in nums:
            freq[ch]=freq.get(ch,0)+1
        for ch in freq:
            if freq[ch]>n//2:
                return ch