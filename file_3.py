def game():
    return 66

score = game()
with open("hiscore.txt","r") as f:
    Hiscore = f.read()

if Hiscore == '':
    with open("hiscore.txt","w") as f:
        f.write(str(score))    

elif int(Hiscore)<score:
    with open("hiscore.txt","w") as f:
        f.write(str(score))
    



