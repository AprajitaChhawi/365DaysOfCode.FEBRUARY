#User function Template for python3

# Function to check if elements are 
# pairwise consecutive in stack 
def pairWiseConsecutive(l):
    a=l[:]
    pair=1
    while a:
        a1=a.pop(0)
        if a:
            b1=a.pop(0)
            if(abs(a1-b1)!=1):
                pair=0
                break;
    return pair
    
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
