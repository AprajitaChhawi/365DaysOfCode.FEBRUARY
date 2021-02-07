# Your task is to complete this function
# Function should return True/False or 1/0
def r(i):
    rev=0
    while(i!=0):
        temp=i%10
        rev=rev*10+temp
        i=int(i/10)
    return rev
def PalinArray(arr ,n):
    for i in arr:
        if (i!=r(i)):
            return False
    return True
    # Code here




#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends
