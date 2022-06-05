#User function Template for python3
class Solution:

	def equilibrium(self,arr, n): 
    	# code here
        total_sum = sum(arr)
        left_sum = 0
        
        for i in arr:
            total_sum-=i
            
            if left_sum == total_sum:
                return "YES"
            left_sum+=i
        return "NO"
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	
	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int , input().strip().split()))
	    ob = Solution()
	    ans=ob.equilibrium(a, n)
	    print(ans)
	    tc=tc-1
# } Driver Code Ends