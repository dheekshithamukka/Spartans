def powerOf2(n):
    if(n!=0):
        return not(n & (n-1))
    
n = int(input())
if(powerOf2(n)):
    print("Yes")
else:
    print("No")