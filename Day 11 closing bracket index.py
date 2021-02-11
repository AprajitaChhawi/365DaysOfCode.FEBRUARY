#User function Template for python3

class Solution:
    def closing (self,s, pos):
        n=len(s)
        count=0
        for i in range(pos,n):
            if s[i]=='[':
                count=count+1
            elif s[i]==']':
                count=count-1
                if(count==0):
                    return i
        # your code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    pos = int (input ())
    ob = Solution()
    print (ob.closing (s, pos))
    
# Contributed By: Pranay Bansal

# } Driver Code Ends
