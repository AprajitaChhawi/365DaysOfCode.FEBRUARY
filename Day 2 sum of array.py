#User function Template for python3

def getSum( arr, n):
    return sum(arr)
    # Your code goes here
    
    




#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(getSum(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
