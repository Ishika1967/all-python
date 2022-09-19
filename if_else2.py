sub1 = int(input("enter the marks of ecad"))
sub2 = int(input("enter the marks of cloud"))
sub3 = int(input("enter the marks of database"))
if((sub1 < 33) | (sub2 < 33) | (sub3 < 33)):
    print("student is fail")
elif(((sub1+sub2+sub3)/3)<40):
    print("student is fail")
else:
    print("student is pass")