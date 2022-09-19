def merge(s,n):
    for part in zip(*[iter(s)] * n):
        # print(part)
        # print(type(part))
        b=set()

        result=[element for element in part if not (tuple(element) in b or  b.add(tuple(element)))]
        #print(str(result))
        
        result = str(result).replace(" ", "")
        l = result[1:-1].split(',')
        print(str(result))
            
s = input("enter the string")
n = int(input("enter the gap"))
merge(s,n)
#print(type(str))
