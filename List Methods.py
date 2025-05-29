#Write atleast 10 Built-in List Functions & Methods with example.
# append
l1 = [1, 2, 3]
l1.append(4)
print(l1)  

# extend
l1 = [1, 2, 3]
l1.extend([4, 5])
print(l1)  
# insert
l1 = [1, 2, 3]
l1.insert(1, 4)
print(l1)  

# remove
l1 = [1, 2, 3, 2]
l1.remove(2)
print(l1)  

# pop
l1 = [1, 2, 3]
item = l1.pop(1)
print(item)  
print(l1)  

# index
l1 = [1, 2, 3, 4]
index = l1.index(3)
print(index)  

# count
l1 = [1, 2, 2, 3, 2]
count = l1.count(2)
print(count)  

# sort
l1 = [3, 1, 2]
l1.sort()
print(l1)  

# reverse
l1 = [1, 2, 3]
l1.reverse()
print(l1)  

# copy
l1 = [1, 2, 3]
copied_l1 = l1.copy()
print(copied_l1)



#Difference between Append, Extend and Insert
l1 = [1, 2, 3]
l1.append(4)
print(l1)

l1 = [1, 2, 3]
l1.extend([4, 5])
print(l1)

l1 = [1, 2, 3]
l1.insert(1, 4)
print(l1)  


