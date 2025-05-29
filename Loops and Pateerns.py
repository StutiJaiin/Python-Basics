i=1
while(i<6):
    if(i==3):
        print(i)
        break
    print(i)
    i+=1
    print("hh")
    
var = 10
while var > 0:
    print ('Current variable value:', var)
    var = var -1
    if var ==5:
        break
print ("Good bye!")                                  #both are examples of break statement

var = 10
while var > 0:
    var = var -1
    if var==5:
        continue
    print('Current variable value:', var)
print("Good bye! ")

i=1
while(i<6):
    i+=1
    if(i==3):
        continue
    print(i)                            #these are both examples of continue statements
    
n=int(input("enter the number"))
for i in range(1,11):
    c=n*i
    print(n,"*",i,"=",c)                 #for loop along with range func; it will give out the table of the entered number

list=['peter','joseph','ricky','devansh']
for i in range(len(list)):               #len function to print the length of the given list
    print("hello", list[i])

rows=int(input("enter the rows:"))
for i in range(1,rows+1):
    for j in range(i):
        print(i,end=' ')                       #to print number pyramid using loops
    print()

rows=int(input("enter the rows"))
for i in range(0,rows+1):
    for j in range(i):
        print("*",end=' ')
    print()
 
