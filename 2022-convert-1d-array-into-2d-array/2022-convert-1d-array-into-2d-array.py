class Solution:
    def construct2DArray(self, arr: List[int], r: int, c: int) -> List[List[int]]:
        if r*c != len(arr):
            return []
        ans = []
        
        for i in range(0,r):
            ans.append(arr[i*c:i*c+c])
        return ans
      
        