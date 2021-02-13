#User function Template for python3
'''
Function Arguments :
		@param  : price( array containing price on days) , n size of list input.
		@return : List containg corresponding span values
'''
def calculateSpan(a,n):
    stack=[]
    s=[]
    for i in range(n):
        while (len(stack)!=0 and a[i]>=a[stack[-1]]):
            stack.pop()
        if len(stack)==0:
            p=-1
        else:
            p=stack[-1]
        stack.append(i)
        s.append(i-p)
    return s
    #code here







#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nikhil Kumar Singh

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        print(*calculateSpan(a, n)) # print space seperated elements of span array
# } Driver Code Ends
