a = [1,2,3,4,11,5,6,13]
cnt = 0
for i in range(0,12,1):
    for j in range(0,len(a)):
        if a[j] == i:
            cnt = cnt +1
            print(f"the element {a[j]} is present in range")
        else:
             continue
             
        
print(cnt)
            
