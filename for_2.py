# num = int(input("enter the num:"))
# for i in range(1,10):
#     print(num*i)

# s = ["harry","Sakshi","Sachin","payal"]
# for item in s:
#     if item.startswith("S"):
#         print("hello"+ " "+ item)

num = int(input("enter the number:"))
prime = True
for i in  range(2,num):
    if(num%i == 0):
        prime = False
        break
    else:
        prime = True

if(prime == True):
    print(num,"is a prime num")
else:
    print(num,"is a composite num")