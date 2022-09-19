s = input("enter the string:")
def Swap(s):
    a = s[0:]
    for a in s:
        if(a.islower()):
            a = a.upper()
        else:
            a = a.lower()
        print(a,end='')   

    
Swap(s)
