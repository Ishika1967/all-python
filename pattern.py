# n = 3
# for i in range(3):
#     print("  "*(n-i-1),end = "")
#     print("* "*((2*i)+1),end = "")
#     print("  "*(n-i-1))
# n = 3
# for i in range(3):
#     print("* "*(i+1))
n= 3
for i in range(3):
   for j in range(i):
       if(j == 2 and i == 2):
           print("  ")
       else:
           print(" * "*n)
    
    