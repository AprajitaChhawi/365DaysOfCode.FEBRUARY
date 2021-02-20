#User function Template for python3

class Solution:
    def profession(self, level, pos):
        c=0
        k=bin(pos-1)
        c=k.count('1')
        if(c%2==0):
            return 'e'
        else:
            return 'd'
            
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        level, pos = [int(x) for x in input().split()]
        
        ob = Solution()
        if(ob.profession(level, pos) == 'd'):
            print("Doctor")
        else:
            print("Engineer")
# } Driver Code Ends
