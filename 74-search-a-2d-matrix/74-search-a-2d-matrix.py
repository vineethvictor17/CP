class Solution:
    def search(self,arr,target,low,high):
            if low>high:
                return False
            mid = (low+high)//2
            if arr[mid] == target:
                return True
            elif arr[mid]>target:
                return self.search(arr,target,low,mid-1)
            else:
                return self.search(arr,target,mid+1,high)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                return self.search(matrix[i],target,0,len(matrix[i])-1)
        
            
            
        