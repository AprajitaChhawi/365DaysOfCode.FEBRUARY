#User function Template for python3

class Solution:
    def largestNum(self,n,s):
        if(9*n<s):
            return -1
        s1=""
        while(s>9):
            s1+='9'
            s=s-9
        s1+=str(s)
        n=n-len(s1)
        k='0'*n
        s1=s1+k
        return s1
            
        '''
        :param n: length of given numberr
        :param s: sum of digits of number
        :return: Integer
        '''
        # code here
    
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
# } Driver Code Ends
