def noOf1(n):
    count = 0
    while(n):
        n &= (n-1)
        count += 1
    return count
    
n = int(input())
print(noOf1(n))