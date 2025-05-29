a=True
b=False
print(a or b)
print(a and b)
print(not a)
a=[1,2,3,4,5]
print(5 in a)
print(4 not in a)
x=5
if type(x) is int:
    print("x is an integer")
else:
    print(" ")
if type(x) is not str:
    print("x is not a string")
else:
    print("x is a string")
a=4
b=5
lesser=a if a<b else b
print(lesser)

help("keywords")
