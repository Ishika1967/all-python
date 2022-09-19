marks = int(input(" enter your marks:"))
if(marks>90 and marks<=100):
    print("grade is Ex")
elif(marks>80 and marks<=90):
    print("grade is A")
elif(marks>70 and marks<=80):
    print("grade is C ")
elif(marks>60 and marks<=70):
    print("grade is D")
elif(marks>=50 and marks<=60):
    print("grade is E")
else:
    print("you are fail")