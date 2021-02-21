#User function Template for python3
class Solution:
	def binaryPalin (self, N):
	    k=bin(N)
	    k=k.replace("0b","")
	    m=''.join(reversed(k))
	    if(k==m):
	        return 1
	    else:
	        return 0
	    
		# Your Code Here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		ob = Solution()
		print(ob.binaryPalin(n))

	# Contributed By: Pranay Bansal

# } Driver Code Ends
