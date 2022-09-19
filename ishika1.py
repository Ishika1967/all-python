a = float(input())
b = float(input())
if(a%5 == 0 and a+0.50<b):
    if(a>b):
        print(b)
    elif(a<b):
        c = b-a-0.50
        b = c
        print(c)
else:
    print(b)