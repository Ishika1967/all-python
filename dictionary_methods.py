myDict={
    "fast": "harry is coder",
    "ishika": "she is a lerner",
    "marks": [1, 2, 3],
    "anotherdict":{'ishi':'player'}
}
print(myDict.keys())# print the keys in the dictionary
print(list(myDict.keys()))
print(list(myDict.values()))
print((myDict.items()))# prints the keys , values for all containts
updateDict = {
    "payal":"divya",
    "fast": "harry a dancer"
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("harry2"))#return None as harry2 is not present in the dictionary
# print(myDict["harry"])# throw error as harry2 is not present in the dict
print(myDict.get("fast"))

