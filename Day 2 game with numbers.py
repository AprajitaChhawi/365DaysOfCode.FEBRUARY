#User function Template for python3

def game_with_number (arr,  n) : 
    for i in range(n-1):
        arr[i]=arr[i]^arr[i+1]
    return arr
    #Complete the function



#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)




# } Driver Code Ends
