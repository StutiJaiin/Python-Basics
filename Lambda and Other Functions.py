def doubler(x):   
    return x*2
print(doubler(2))    #anonymous function or labmda function

doubler=lambda x:x*2
print(doubler(2))

mul=lambda x,y:x*y
print(mul(2,5))   #we can pass multiple arguments through a lambda function and just seperate them using a comma

add = lambda x,y,z: x+y+z
print(add(2,3,4))      #positional arguments

add=lambda x,y,z: x+y+z
print(add(2, z=3, y=4))   #keyword arguments

add=lambda x, y= 3, z= 4: x+y+z
print(add(2))                 #default arguments

add=lambda *args: sum(args)
print(add(2,3,5,7))     #variable list of arguments

add=lambda**kwargs:sum(kwargs.values())
print(add(x=2, y=3, z=3, f=8))     #variable list of keyword arguments

findMin=lambda x, y: x if x <y else y     #if else with lambda function
print(findMin(2,4))
print(findMin('a','x'))

def doubler(x):
    return x*2
L=[1,2,3,4,5,6]
listmod=map(doubler,L)  #map functions takes two arguments, a function and a list; it applies the function on every item of the list and then returns the modified list
print(list(listmod))        


l=[1,2,3,4,5,6]
doubler=map(lambda x:x*2,L)
print(list(doubler))       #this is a map function to double each item of the list


py_list = ['e','a','i','o','u']
print(sorted(py_list)) #sorted function for list

py_string= 'python'
print(sorted(py_string))   #sorted function for string

py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))    #sorted function for tuple

py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))    #sorted function for set

py_dict = {'e': 1, 'a':2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(py_dict, reverse=True))     #sorted function for dictionary

def func(x):
    return x % 7
L=[15, 3, 11, 7]
print ("Normal sort :", sorted(L))
print ("Sorted with key:", sorted(L, key = func))           #sorting functions

dict = {}
dict['1'] = 'apple'
dict['3'] = 'orange'
dict['2'] = 'mango'
lst = dict.keys()                      #sorted by key
print("Sorted by key: ", sorted(lst))

dict ={}
dict['1'] = 'apple'
dict['3'] = 'orange'
dict['2'] = 'mango'
lst = dict.values()                    #sorted by value
print("Sorted by value: ", sorted(lst))

dict ={}
dict['1'] = 'apple'
dict['3'] = 'orange'
dict['2'] = 'mango'
lst = dict.items()                        #sorted by item
print("Sorted by value: ", sorted(lst))


def checkAge(age):
    if age > 18:
        return True
    else:
        return False

age = [5, 11, 16, 19, 24, 42]
adults = filter(checkAge, age)
print(list(adults))                              #filters the age above 18

age = [5, 11, 16, 19, 24, 42]
adults = filter(lambda x: x > 18, age)
print(list(adults))

x = "global"
def foo():
    print("x inside:", x)
foo()
print("x outside: ", x)                       #declaration of global variables outside and inside a function



x = 5                #global
def foo():
    x = 10               #local
print("local x:", x)
foo()
print("global x:", x)                   #we can declare local and global variable with the same names

def outer(name):                     #this is the enclosing function
    def inner():
        print(name)
    inner()                          #call the enclosing function
outer('Tech')






