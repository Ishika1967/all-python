class Employee:
    company = "Google"
    def __init__(self):
        print("this is my first oop programm in python")
    def companyname(self,company):
        print(f"name of the company is {company}")
    def info(self,emname,salary):
        self.emname = emname
        self.salary = salary
        print(f"name is {emname} and salary is {salary}")
class Lowemployee(Employee):
    def __init__(self):
        super().__init__()
        print(f"my company is same as employee{Employee.company}")
    def selfish(self):
        print("HEllo")
a = Employee()
b = Lowemployee()
print(b.info("ishika",100000))
b.selfish()
b.companyname("AWS")
b.info("prachi", 1000000)
a.info("preeti", 1000000)
