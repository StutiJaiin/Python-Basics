def func():
    print("hello from the function")
func()
def greet():
    """This function displays 'Hello World! """

print('Hello World!')
greet()
val= greet()
print(val)   #the output will be none because the return statement does not exist
def func1(f1):
    print(f1+"ref")
func1("f1")
func1("f3")
func1("f4")  #these are the information/parameters passed into a function

def func2(*letters):
    print("the names of the function are" +letters[2])
func2("f1","f2","f3")
    
def my_function (child3, child2,child1):
    print("The youngest child is " +child3)
my_function(child1="a", child2="b", child3="c")   #this complete code will print "the youngest child is c" #keyword arguments

def func3(**kid):
    print("his last name is " +kid["lname"])
func3(fname="T",lname="R")    #if the number of keyword argument is unknown add a **


def func4 (country="norway"):
    print("I am from "+ country)
func4 ("sweden")
func4 ("india")
func4 ()
func4("brazil")  #calling a function without the parameter

def func5(food):
    for x in food:
        print(x)
    print(type(food))

fruits=["apple","banana","cherry"]   #we can also pass a list as an argument as well
func5(fruits)

def func6(x):
    return 6*x
    print(func6(3))
n=func6(3)
print(func6(5))
print(func6(6))    #this is an example of the use of return statement

def func7():
    pass     #if we have a function wihtout any content, we can add pass so that it doesn't give any errors

def add(n1, n2):
    return n1+n2
sum1=add(100,200)
sum2=add(8,9)
print(sum1)
print(sum2)   #this is an example for add() function

def factorial(num):
    if num==1:
        return 1
    else:
        return (num*factorial(num-1))
    num=5
    print("factorial of", num, "is:", factorial(num))

