def variableArgs(*a):# we use pointer beacuse we dont no the length odf variables
    print("elements are:")
    for ele in a: #to print the elements one by one
        print(ele)
    print(a[2])  # we can access the elements as a array elements
    return
    
variableArgs(10,20,30,'ishika')
