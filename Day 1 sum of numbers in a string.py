#User function Template for python3


'''
	Your task is to return the sum of all the
	numbers appearing in the given string.
	
	Function Arguments: s (given string)
	Return Type: integer

'''
import re
def findSum(s):
    a=[]
    a=[int(i) for i in re.split("[a-z]",s) if i.isdigit()]
    return sum(a)
            
            
        
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
