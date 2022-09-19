b = set()
b.add(2)
b.add(5)
b.add(4)
b.add(5)
print(b)
# b.add([4,5,6])#unhashable type list i.e we can not add list in the set but we can add tuple in the sets
b.add((11,22,33,44))
print(b)