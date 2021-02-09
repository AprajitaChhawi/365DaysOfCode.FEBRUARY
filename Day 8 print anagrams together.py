#User function Template for python3

def Anagrams(words,n):
    d={}
    for i in words:
        x=''.join(sorted(list(i)))
        if x in d:
            d[x].append(i)
        else:
            d[x]=[i]
    return sorted(d.values())
    #code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ans=Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends
