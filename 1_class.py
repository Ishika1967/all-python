class Ishika:
    def __init__(self, name, age) :
        self.Sname = name
        self.Iage = age
    def DevOps(self, post):
        return "post is {}".format(post)
a = Ishika("payal", 22)
print(f" name is {a.Sname} and age is {a.Iage}")
print(a.DevOps("Tech  lead DevOps"))