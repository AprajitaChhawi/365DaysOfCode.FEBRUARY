#User function Template for python3

'''
Function Arguments :
		@param  : S (given postfix expression)
		@return : return the desired value
'''
def EvaluatePostfix(S):
    stack = []
    for i in S:
        if i in "+*-/":
            op1 = stack.pop()
            op2 = stack.pop()
            if i == '+':
                stack.append(op2 + op1)
            elif i == '-':
                stack.append(op2 - op1)
            elif i == '*':
                stack.append(op2 * op1)
            elif i == '/':
                stack.append(int(op2 / op1))
        else:
            stack.append(int(i))
    return stack[0]


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
        print('{0:g}'.format(float(EvaluatePostfix(exp))))
# } Driver Code Ends
