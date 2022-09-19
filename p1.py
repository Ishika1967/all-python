f = "ishiketa willet definitely gets a 9 lpa job "
s = "et"
print(len(f))
if s in f:
    print(f"found at {f.index(s)}")
else:
    print("not found")
print(f.count(s))