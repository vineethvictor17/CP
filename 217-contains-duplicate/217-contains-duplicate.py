class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        for i in nums:
            if i not in a:
                a.add(i)
        
        if len(nums) != len(a):
            return True
        
        return False
       