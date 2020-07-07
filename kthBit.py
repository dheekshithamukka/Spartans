def kthBit(n,k):
    temp = n & (1 << (k-1))
    if(temp):
        print("SET")
    else:
        print("NOT SET")
    
    
n = int(input())
k = int(input())
kthBit(n,k)