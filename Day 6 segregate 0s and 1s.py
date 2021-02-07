#User function Template for python3

class Solution:
    def segregate0and1(self, arr, n):
        c1=arr.count(0)
        c2=arr.count(1)
        if(c1==n or c2==n):
            return arr
        else:
            i=0
            while(c1):
                arr[i]=0
                i=i+1
                c1=c1-1
            while(c2):
                arr[i]=1
                i=i+1
                c2=c2-1
        return arr
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregate0and1(arr, n)
        print(*arr)
        tc -= 1

# } Driver Code Ends
