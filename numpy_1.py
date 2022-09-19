# import numpy
# N = int(input())
# M = int(input())
# print (numpy.eye(N,M,k= 0))
import numpy
numpy.set_printoptions(legacy='1.13')
x, y = input().split()

print (numpy.eye(int(x),int(y),k= 0))