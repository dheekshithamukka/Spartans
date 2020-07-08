def rev(n):
    size = 32
    binary = bin(n)
    reverse = binary[-1:1:-1]
    reverse = reverse + (size-len(reverse))*'0'
    print(int(reverse,2))

n = int(input())
rev(n)