#User function Template for python3
class Solution:
	def isPlaindrome(self, S):
	    k=[]
	    l=len(S)
	    mid=l//2
	    for i in range(mid):
	        k.append(S[i])
	    if(l%2==0):
	        for i in range(mid,l):
	            temp=k.pop()
	            if(temp!=S[i]):
	                return 0
	        return 1
	    else:
	        for i in range(mid+1,l):
	            temp=k.pop()
	            if(temp!=S[i]):
	                return 0
	        return 1
		# code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPlaindrome(S)
		print(answer)

# } Driver Code Ends
