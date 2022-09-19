t = []
a = []
n = int(input("enter no of elements:"))
d = int(input("by how many position the rotation is needed:"))
for i in range(0,n):
    x = int(input("ele:"))
    a.append(x)
while(k<d):
    t.append(a[k])
    a.remove(a[k])
    k = k+1




