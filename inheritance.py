class Person(object):
    def __init__(self,name,personid):
        self.name=name
        self.personid=personid
    
    def display(self):
        print(self.name)
        print(self.personid)

class Employee(Person):
    def __init__(self,name,personid,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,personid)
    
a = Employee("Ali", 1062, "$45000", "ITO Level 1")

a.display()


class Person(object):
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def display(self):
        print(self.firstname)
        print(self.lastname)

class Student(Person):
    def __init__(self,fname,lname,gradyear):
        super().__init__(fname,lname)
        self.graduationyear=gradyear

x = Student("Hamza", "Naqvi", 2023)
x.display()
print(x.graduationyear)