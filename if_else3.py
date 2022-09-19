# spam = ["make a lot of money","buy now","subscribe this","click this"]
s = input("enter the message:")
if("make a lot of money" in s):
    spam = True
elif("buy now" in s):
    spam = True
elif("subscribe this" in s):
    spam = True
elif("click this" in s):
    spam = True
else:
    spam = False

if(spam == True):
    print("this text is spam")
else:
    print("no spam")
    
    