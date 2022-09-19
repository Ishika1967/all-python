n = int(input("enter the size of array:"))
d = int(input("shifting by :"))
arr = []
temp =0
for i in range(0,n):
    x = int(input("enter ele:"))
    arr.append(x)
def reverse_list(arr,s,e):
    while(s<e):
        temp = arr[s]
        arr[s] = arr[e]
        arr[e] = temp
        s=s+1
        e= e-1
def rotate(arr,d):
    if d == 0:
        return
    n = len(arr)
    d =d %n
    reverse_list(arr,0,d-1)
    reverse_list(arr,d,n-1)
    reverse_list(arr,0,n-1)
def printarray(arr):
    for i in range(0,n):
        print(arr[i])
rotate(arr,d)
printarray(arr)
        