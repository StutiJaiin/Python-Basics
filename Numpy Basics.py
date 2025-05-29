#Convert numbers =[1, 2.0, 3] to numpy array and convert all elements to string type.
import numpy as np

numbers = [1, 2.0, 3]
arr = np.array(numbers, dtype=str)
print(arr)

#Create a 2 D array through list and set dtype as int32
array_2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print(array_2d)


#Find the rows and columns of the 2d array created in part b
rows, cols = array_2d.shape
print("Rows:", rows)
print("Columns:", cols)

#Print 10 random numbers between 1 and 100.
random_numbers = np.random.randint(1, 101, size=10)
print(random_numbers)

#Write a NumPy program to get help on the add function
help(np.add)

#Write a NumPy program to test whether none of the elements of a given array is zero
arr = np.array([1, 2, 3])
print(np.all(arr))

#Write a NumPy program to test whether any of the elements of a given array is non-zero
arr = np.array([0, 0, 5])
print(np.any(arr))

#Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution
normal_dist = np.random.randn(15)
print(normal_dist)
