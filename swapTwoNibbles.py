def intToBin(n):
    b = bin(n).replace("0b", "")
    nu = "0"+b
    s1 = nu[:4]
    s2 = nu[4:]
    s1 , s2 = s2 , s1
    num = s1 + s2
    print(int(num, 2))
    
n = int(input())
intToBin(n)