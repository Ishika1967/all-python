l1 = ["mote","donkey"]
with open("new.txt") as f:
    content = f.read()

for word in l1:
    content = content.replace(word,"itelligent")
    with open("new.txt","w") as f:
            f.write(content)



