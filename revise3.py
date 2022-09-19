n = int(input())
arr = map(int, input().split())
l=[]
l.append(arr)
    
res = []
for i in l:
    if i not in res:
        res.append(i)
res.sort()
   
k = len(res)
print(res)
    
    