a = int(input("enter thr first number:"))
s = 0
x = a

def count(a):
    c = 0
    while(a > 0):
        c =c +1
        a =a//10
    return c

        
    
# print(count(a))
# n = 1
# for i in range(1,5s):
#     n=3*n
 
for i in range(count(a)):
    d = a%10
    s = s+(d*d)
    a = a//10
    print(int(s))
if(x == s):
    print(" number is armstrong")
else:
    print(" not armstrong")
    