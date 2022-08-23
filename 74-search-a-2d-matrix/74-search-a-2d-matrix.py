class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [
            # [1,3,5,7],
            # [10,11,16,20],
            # [23,30,34,60]
            # ]
        
        # target = 3
        lst = []
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                lst.append(matrix[row][col])
        
        for i in lst:
            if target in lst:
                return True
            else:
                return False
        
        
            
            
        