class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intr1=[]
        for i in nums1:
            if i in nums2:
                intr1.append(i)
                nums2.remove(i)
        return intr1