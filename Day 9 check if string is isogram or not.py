#User function Template for python3

#Complete this function
def isIsogram(s):
    k=set(s)
    for i in k:
        if s.count(i)>1:
            return False
    return True
            
    #Your code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3




def main():
    T=int(input())
    
    while(T>0):
        
        s=input()
        if isIsogram(s) is True:
            print(1)
        else:
            print(0)
        T-=1


if __name__=="__main__":
    main()
# } Driver Code Ends
