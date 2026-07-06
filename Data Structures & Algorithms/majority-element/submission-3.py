class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for ch in nums:
            freq[ch]=freq.get(ch,0)+1
        return max(freq,key=freq.get)