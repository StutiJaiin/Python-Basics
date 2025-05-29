l = []

for i in range(1, 51):
    l.append(i * i)

print("List with square of integers from 1 to 50:")
print(l)                                                #program 1(to print the squares of all the numbers from 1 to 50)

def count_characters(string):
    count = 0
    for char in string:
        if char.isalpha():
            count += 1
    return count

# Define the input string
input_string = "***Hello, World!***"
print("Input string:", input_string)

result = count_characters(input_string)
print("Number of characters:", result)                                                                   #program 2(count the number of strings

string="reverse"
rev=string[::-1]
print(rev)                                                         #program 3(print a string in reverse)



def is_armstrong(num):
    sum_of_cubes = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10
    return sum_of_cubes == num
print("Armstrong numbers between 1 and 1000:")
for i in range(1, 1001):
    if is_armstrong(i):
        print(i)                                                   #program 4(print armstrong numbers between 1 to 1000)

