# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         l , r = 0, len(numbers) - 1
#         while l<r:
#             currsum = numbers[l] + numbers[r]
#             if currsum > target:
#                 r-=1
#             elif currsum < target:
#                 l+=1
            
#             else:
#                 return[1+1,r+1]
#         return []
    
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]    
        
        