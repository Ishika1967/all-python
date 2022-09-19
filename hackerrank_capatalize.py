import math
import os
import random
import re
import sys
def solve(s):
    r = []
    r = s.split()
    #print(r)
    for i in range(len(r)):
        #print(r[i])
        print(r[i].title(),end=" ")
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
