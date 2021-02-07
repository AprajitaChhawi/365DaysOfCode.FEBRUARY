#User function Template for python3
class Solution:

	def matchPairs(self,nuts, bolts, n):
	    d={}
	    for i in range(n):
	        d[nuts[i]]=i
	    for i in range(n):
	        if bolts[i] in d:
	            bolts[i]=nuts[i]
	    nuts.sort()
	    bolts.sort()
	   
		# code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
