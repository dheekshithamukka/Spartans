def kadane(arr):
    ma = 0
    maxEnd = 0
    for i in arr:
        maxEnd = maxEnd + i
        maxEnd = max(maxEnd, 0)
        ma = max(ma, maxEnd)
    print(ma)

arr = [int(i) for i in input().split()]
kadane(arr)