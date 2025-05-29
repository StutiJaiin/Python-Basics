#Generate squares of all the integers from 1 to 50.def square(n, current=1):
def square(n, current=1):
    if current > n:
        return []
    return [current**2] + square(n, current + 1)

squares = square(50)
print(squares)

#Count the number of characters in a string using a loop.
def count_characters(s):
    count = 0
    for char in s:
        count += 1
    return count

string = "Hello, World!"
result = count_characters(string)
print(result)
