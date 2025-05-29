#destructor
class Example:
    def __init__(self):
        print ("Object created")
    def __del__(self):
        print ("Object destroyed")
myObj = Example()
del myObj


#inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("dog barking")
d = Dog()
d.bark()
d.speak()

#multilevel inheritance
class Animal:
    def run(self):
        print("Animal running")
class Dog(Animal):
    def bark(self):
        print("dog barking")
class Puppy(Dog):
    def eat(self):
        print("Eating bread...")
p = Puppy()
p.bark()
p.run()
p.eat()


#multiple inheritance
class Calculation1:
    def summation(self, a, b):
        return a + b
class Calculation2:
    def multiplication(self, a, b):
        return a * b
class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a / b
d = Derived()
print(d.summation(10, 20))
print(d.multiplication(10, 20))
print(d.divide(10, 20))


#hierarchial inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()



#checking for inheritance
class Calculation1:
    def summation(self, a, b):
        return a + b
class Calculation2:
    def multiplication(self, a, b):
        return a * b
class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a / b
d = Derived()
print(issubclass(Derived, Calculation2))
print(isinstance(d, Calculation1))


