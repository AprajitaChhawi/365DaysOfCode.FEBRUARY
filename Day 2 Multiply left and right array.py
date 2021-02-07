#User function Template for python3

def multiply (arr, n) :
    mid=n//2
    l1=sum(arr[:mid])
    l2=sum(arr[mid:])
    return l1*l2
    #Complete the function




#{ 
#  Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = multiply(arr, n)
    print(ans)
# } Driver Code Ends
