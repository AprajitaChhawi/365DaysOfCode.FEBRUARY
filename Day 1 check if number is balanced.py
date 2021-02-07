#User function Template for python3
class Solution:
	def balancedNumber(self, N):
	    k=[]
	    for i in N:
	        k.append(int(i))
	    mid=(len(N)//2)
	    if(sum(k[:mid])==sum(k[mid+1:])):
	        return True
	    else:
	        return False
		# your code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		N = input ()
		ob = Solution()
		if ob.balancedNumber(N):
			print (1)
		else:
			print (0) 
# } Driver Code Ends
