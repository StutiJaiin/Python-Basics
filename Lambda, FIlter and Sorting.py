#Get some numeric element in a list and find the sum of elements of list using map and lambda function
list1=[1,2,3,4,5,6,7,8,9]
print(list1)
maps=map(lambda x:x,list1)
totalsum=sum(maps)
print(totalsum)


#Get the age of students in a list and display those students who are above 18, use lambda and filter function.

ages=[18,19,20,21,16,17,22,17,24]
print(ages)
adults=list(filter(lambda x: x >18, ages))
print(adults)

'''Get the name and age of students from user in a dictionary and return two different dictionary where entry of dictionary are sorted by name and age respectively. Use customized sorted()
function'''


def custom_sort(dictionary, key_index):
    return dict(sorted(dictionary.items(), key=lambda item: item[key_index]))

dict_students = {"stuti": 19, "ayush": 20, "niharika": 18, "rashi": 19}
print("Original dictionary:")
print(dict_students)


sorted_by_name = custom_sort(dict_students, 0) 
sorted_by_age = dict(sorted(dict_students.items(), key=lambda item: item[1]))  


print("\nDictionary sorted by name:")
print(sorted_by_name)

print("\nDictionary sorted by age:")
print(sorted_by_age)


#Demonstrate the concept of closure function

def outer(name):
    def inner():
        print(name)
    inner()
outer('Tech')
