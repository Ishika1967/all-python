n = int(input())
arr = map(int, input().split())
a = set(arr)
b = list(a)
maxi =b[0]
for i in range(0,len(b)):
    if(b[i]>maxi):
        maxi = b[i]
b.remove(maxi)
    #print(b)
c = tuple(b)
    #print(c)
print(c[-1])
