#User function Template for python3

def countOfElements( a, n, x):
    count=0
    for i in range(n):
        if(a[i]<=x):
            count=count+1
        else:
            break
    return count
    





#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        print(countOfElements(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
