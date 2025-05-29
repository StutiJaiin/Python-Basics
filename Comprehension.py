l1=[1,2,3,4,5,6]
lc=[var for var in l1 if var%2==0]
print("output list using comprehension: ", lc)   #this is an easier to way to print a few elements of an already existing list, it is called list comprehension; lc is the comprehended list

list=[1,2,3,3,4,4,4,5,6,7,7,8,8]
sc={var for var in list if var %2==0}
print("output set using comprehension: ", sc)  #this is set comprehension, similar to list comprehension expect for {} brackets

listdc=[1,2,3,4,5,6,7]
dc={var:var**3 for var in listdc if var % 2!=0}
print("output dictionary using comprehension", dc)   #this is dictionary comprehension to print the odd numbers and their cubes




