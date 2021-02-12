#User function Template for python3

''' Your task is to check if the given string is
	a panagram or not.
	
	Function Arguments: s (given string)
	Return Type: boolean
'''
def checkPangram(s):
    k=set()
    s=s.lower()
    t=s.replace(',','')
    h=t.replace(' ','')
    for i in h:
        if str(i)>='a' or str(i)<='z':
            k.add(i)
    return len(k)==26



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
        if(checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
