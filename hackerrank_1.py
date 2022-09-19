import math
import os
import random
import re
import sys



n = int(input("enter the number: "))
m = n%2;
while n > 0:
    {
        if(m == 0):
            {
                if(n>=2 and n<=5):
                    print("Not Wierd")
                elif(n >= 6 and n <= 20):
                    print("Wierd")
                else:
                    print("Not Wierd")
                    
            }
        else:
            print("Wierd")
                    
    }