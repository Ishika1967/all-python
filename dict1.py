d = { 10:"a",20:"b",30:"c",40:"d",50:"e"}
print(d)
print(d.keys())
print(d.values())
d.popitem()
print(d)
d.pop(20)
print(d)
d.update({60:"f"})
print(d)
for key in d:
    values = d.get(key)
    print(values)