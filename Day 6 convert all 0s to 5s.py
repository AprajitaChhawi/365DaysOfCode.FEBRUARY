# Function should return an integer value
def convertFive(n):
    x=n
    i=0
    while(x!=0):
        temp=x%10
        i=i+1
        if(temp==0):
            k=i-1
            n=n+5*(10**k)
        x=x//10
    return n
    # Code here



#{ 
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
# } Driver Code Ends
