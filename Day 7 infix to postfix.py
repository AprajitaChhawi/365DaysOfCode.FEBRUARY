#User function Template for python3
'''
Function Arguments :
		@param  : exp (given infix expression)
		@return : string
'''
def InfixtoPostfix(exp):
    d={}
    d['^']=4
    d['*']=3
    d['/']=3
    d['+']=2
    d['-']=2
    d['(']=1
    post=""
    l=[]
    for i in exp:
        if i.isalpha():
            post+=i
        elif i=='(':
            l.append(i)
        elif i==')':
            top=l.pop(-1)
            while(top!='('):
                post+=str(top)
                top=l.pop(-1)
        else:
            while(len(l)>0 and d[l[-1]]>=d[i]):
                post+=str(l[-1])
                l.pop()
            l.append(i)
    while(len(l)!=0):
        temp=l[-1]
        post+=str(temp)
        l.pop()
    return post
            
    
    #code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


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
        exp = str(input())
        print(InfixtoPostfix(exp))
# } Driver Code Ends
