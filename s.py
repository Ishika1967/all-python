n = int(input("enter no of elements:"))
d = int(input("by how many position the rotation is needed:"))
t = []
a = []
#k =0
for i in range(0,n+1):
    x = int(input("ele:"))
    a.append(x)
for k in range(0,d-1):
    t.append(a[k])
    a.remove(a[k])
a.append(t)
print(a)
# for i in t:
#     a.append(i)
# print(a)



