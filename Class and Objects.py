class car:                                                    #creating a class(like a building)
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year
    def display(self):
        print(self.modelname,self.year)
c1=car("Toyota", 2016)
c1.display()                                                #c1 is the object

class Employee:
    name='TCS'
    id="CI23"
    def display (self):
        print(self.id,self.name)

#here the class is employee, with two fields: id and name; the function is display()

class Employee:
    id='C123'
    name="tcs"
    def display(self):
        print("ID: ", self.id,"Name: ", self.name)
    emp=Employee()
    emp.display()
#creating "emp" instance for employee class

class Student:
    name='TCS'                  #class variable
    id='C123'                   #class variable
    def display_details(self):
        print("Name: ", self.name,"ID: ", self.id, "age: ", self.age)
s=Student()
s.name='amit'                       #instance variable
s.id=112                                 #instance
s.age=23                            #instance
s.display_details()
print(Student.name)
print(Student.id)
s2=Student()
print(s2.name)

class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name
    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))
emp1 = Employee("Gagan", 101)
emp2 = Employee("Kavita", 102)
emp1.display()
emp2.display()

class Student:

    def __init__(self):
        print("This is non parametrized constructor")
    def show(self,name):
        print("Hello",name)
student = Student()
student.show("Susheel")
    
