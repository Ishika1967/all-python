a = [ 10, 20 ,30 ,40 ,50]
# print(a)  #[ 10, 20 ,30 ,40 ,50]
# print(a[-1]) #50
# print(a[5:-5]) #[] list cannot be reversed by slicing
# print(a[-5:5]) #[ 10, 20 ,30 ,40 ,50]
# print(a[:3])   #[10,20,30]
# print(a[:])  #[ 10, 20 ,30 ,40 ,50]
a.append(60)
print(a)
a.insert(2,70)
print(a)
a.insert(10,100)
print(a)
a.pop(3)
print(a)
a.remove(20)
print(a)
print()