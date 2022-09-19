def merge(s,n):
    str = ''  # initializing the empty string  
  
    for i in s: #Iterating and adding the list element to the str variable  
        str += i  
  
    print(str) 
s = input(" enter the string:")
n = int(input("enter the gap element:")) 
merge(s,n)
