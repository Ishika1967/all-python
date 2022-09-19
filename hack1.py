n = int(input("enter the number:"))
while(n>0):
    {
        if n%2 == 0:
            {
                if(n in range(2,6) or n>20):
                    print("Not Wierd")
                elif(n>=6 and n<=20):
                    print("Wierd")
            }
        else:
            print("Wierd")
    }