class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1+nums2
        a.sort()
        total=len(a)
        if total%2==1:
            return float(a[total//2])
        else:
            mid1=a[total//2-1]
            mid2=a[total//2]
            return (float(mid1+mid2)/2.0)
