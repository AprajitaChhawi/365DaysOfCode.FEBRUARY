def max_of_subarrays(arr,n,k):
    l=[]
    for i in range(0,n-k+1,1):
        l.append(max(arr[i:i+k]))
    return l
l=[1,2,3,1,4,5,2,3,6]
p=max_of_subarrays(l,9,3)
print(p)
