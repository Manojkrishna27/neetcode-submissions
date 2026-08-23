class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res=[]
        res1=[]
        for ch in nums:
            if ch%2==0:
                res.append(ch)
            if ch%2!=0:
                res1.append(ch)
        return res+res1