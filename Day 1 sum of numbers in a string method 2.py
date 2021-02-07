#User function Template for python3


'''
	Your task is to return the sum of all the
	numbers appearing in the given string.
	
	Function Arguments: s (given string)
	Return Type: integer

'''

def findSum(s):
    temp="0"
    p=0
    for i in s:
        if(i.isdigit()):
            temp=temp+i
        else:
            p=p+int(temp)
            temp="0"
    return p+int(temp)
        
    #code here







#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        print(findSum(s))
# } Driver Code Ends
