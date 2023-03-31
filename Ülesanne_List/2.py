# https://www.geeksforgeeks.org/python-program-to-convert-binary-to-hexadecimal/
  
def binToHexa(n):
    bnum = int(n)
    temp = 0
    mul = 1
    count = 1
    hexaDeciNum = ['0'] * 100
    i = 0
    while bnum != 0:
        rem = bnum % 10
        temp = temp + (rem*mul)
        if count % 4 == 0:
            if temp < 10:
                hexaDeciNum[i] = chr(temp+48)
            else:
                hexaDeciNum[i] = chr(temp+55)
            mul = 1
            temp = 0
            count = 1
            i = i+1
        else:
            mul = mul*2
            count = count+1
        bnum = int(bnum/10)
    if count != 1:
        hexaDeciNum[i] = chr(temp+48)
    if count == 1:
        i = i-1
    print("Sisend (binaar): {}    Väljund(16-süsteem): ".format(n), end="")
    while i >= 0:
        print(end=hexaDeciNum[i])
        i = i-1

loend = "110"

binToHexa(loend)