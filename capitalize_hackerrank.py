s = input("enter the string:")
def solve(s):
    r = []
    r = s.split()
    #print(r)
    for i in range(len(r)):
        #print(r[i])
        print(r[i].title(),end=" ")
print(solve(s))