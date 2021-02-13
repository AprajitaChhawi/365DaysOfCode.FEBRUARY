#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        n=len(S)
        stack=''
        for i in range(0,n):
            if(len(stack)==0):
                stack=stack+S[i]
            if(stack[-1]!=S[i]):
                stack=stack+S[i]
        return stack
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends
