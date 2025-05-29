
a = 5
b = 10
c = 15
sum_of_numbers = a + b + c
print(f"(a) Sum of three numbers: {sum_of_numbers}")




string1 = "Hello, "
string2 = "World!"
concatenated_string = string1 + string2
print(f"(b) Concatenated strings: {concatenated_string}")




length = 10
width = 5
area_of_rectangle = length * width
print(f"(c) Area of rectangle: {area_of_rectangle}")




import math
radius = 7
area_of_circle = math.pi * radius ** 2
print(f"(d) Area of circle: {area_of_circle:.2f}")


number = 27
cubic_root = number ** (1/3)
print(f"(e) Cubic root: {cubic_root:.2f}")



a = 10
b = 20
c = 30
average = (a + b + c) / 3
print(f"(f) Average of three numbers: {average:.2f}")

print("-------------------------------------------------------")

a = 5
b = 10
a = a + b
b = a - b
a = a - b
print(f"(g) After swapping: a = {a}, b = {b}")




string = "Python"
string_length = len(string)
reversed_string = string[::-1]
uppercase_string = string.upper()
print(f"(h) String length: {string_length}, Reversed: {reversed_string}, Uppercase: {uppercase_string}")


number = 7
if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"
print(f"(i) The number {number} is {result}")


marks = [90, 85, 78, 88, 92]
average_marks = sum(marks) / len(marks)

if 91 <= average_marks <= 100:
    grade = "O"
elif 81 <= average_marks <= 90:
    grade = "A+"
elif 71 <= average_marks <= 80:
    grade = "A"
elif 61 <= average_marks <= 70:
    grade = "B+"
elif 51 <= average_marks <= 60:
    grade = "B"
elif 41 <= average_marks <= 50:
    grade = "C+"
elif 35 <= average_marks <= 40:
    grade = "C"
else:
    grade = "Fails"

print(f"(j) Average marks: {average_marks:.2f}, Grade: {grade}")

x=40
if(x > 10):
    print("Above ten,")
    if x > 20:
        print("and also above 201")
    else:
        print("but not above 20.")
else:
    print("not greater than 10")
