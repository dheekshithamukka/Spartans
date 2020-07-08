def minXOR(a,n):
    a.sort()
    mi = 2**30
    t = 0
    for i in range(0, n-1):
        t = a[i] ^ a[i+1]
        mi = min(mi,t)
    return mi
 
arr = list(map(int, input().strip().split()))
n = len(arr)
print(minXOR(arr,n))