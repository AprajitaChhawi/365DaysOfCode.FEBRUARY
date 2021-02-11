#User function Template for python3
class Solution:
	def penaltyScore(self, S):
	    count=0
	    l=len(S)
	    for i in range(0,l-1):
	        if(S[i]=='2' and S[i+1]=='1'):
	            count=count+1
	    return count
		# code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.penaltyScore(S)
		
		print(answer)


# } Driver Code Ends
