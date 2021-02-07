#User function Template for python3
import math
# Function to check if elements are 
# pairwise consecutive in stack 
def pairWiseConsecutive(l):
    top=0
    s=l[:]
    top=len(l)
    if((top%2)!=0):
        s.pop()
    while(len(s)!=0):
        temp1=s.pop()
        temp2=s.pop()
        if(abs(temp1-temp2)!=1):
            return False
    return True
    #add code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        pairWiseConsecutive(l)
        if(pairWiseConsecutive(l)==True):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends
