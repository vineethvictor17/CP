#User function Template for python3

def isSubset( a1, a2, n, m):
    s = set()
    for i in range(n):
        s.add(a1[i])
    l = len(s)
    
    for i in range(m):
        s.add(a2[i])
    
    if l == len(s):
        return "Yes"
    return "No"
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends