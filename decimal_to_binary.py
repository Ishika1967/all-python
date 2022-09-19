n = int(input("enter no:"))
def binaryToDecimal(n):
    l = []
    while(n>0):
        dig = n%2
        l.append(dig)
        n = n//2
    l.reverse()
    #return l
    for i in range(0,len(l)):
        print(l[i],end=" ")
binaryToDecimal(n)
