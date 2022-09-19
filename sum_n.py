# def sum(n):
#     s = 0;
#     for i in range(n+1):
#         s = s + i;
#     return print(s) 
# sum(10)
def sum(n):
    if( n==1):
        return 1
    else:
        return sum(n-1)+n
d = sum(10)
print(d)