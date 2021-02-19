#User function Template for python3

class Solution:
    def countWords(self,List, n):
        d={}
        count=0
        v=0
        for i in List:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d.values():
            if i==2:
                v=v+1
        return v
                
        #code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        List = input().split()
        ob = Solution()
        print(ob.countWords(List, n))
# } Driver Code Ends
