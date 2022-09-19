import random
def game(comp, you):
    if comp == you:
        return None
    
    elif comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False

    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

    elif comp =='g':
        if you == 'w':
            return True
        elif you == 's':
            return False
    
print("computer turn : snake(s),water(w),gun(g):")
select = random.randint(1, 3)
if select == 1:
    comp = 's'
elif select == 2:
    comp = 'w'
elif select == 3:
    comp = 'g'

you = input("enter your chioce:")
a =  game(comp,you)

print(f"comp choose {comp}")
print(f"you chose {you}")
if a == None:
    print("tie")
elif a:
    print("you won")
else:
    print("you loose")

