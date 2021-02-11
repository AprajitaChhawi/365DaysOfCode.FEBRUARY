#User function Template for python3
class Solution:
	def barcketNumbers(self, S):
	    count=0
	    k=[]
	    a=set()
	    l=[]
	    for i in S:
	        if i=='(':
	            count=count+1
	            l.append(count)
	            k.append(count)
	        elif i==')':
	            k.append(l[-1])
	            l.pop()
	           
	    return k
	        
	        
		# code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.barcketNumbers(S)
		for value in answer:
			print(value, end = " ")
		print()


# } Driver Code Ends
