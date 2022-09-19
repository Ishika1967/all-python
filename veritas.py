import math
a = int(input("enter no:"))
def isperfect(a):
    x = math.sqrt(a)
    return a == x*x
def isfibo(a):
    return (isperfect(5*a*a+4) or isperfect(5*a*a-4))
if (isfibo(a) == True):
    print(f"{a} is a fibo number")
else:
    print("number is not fibo")