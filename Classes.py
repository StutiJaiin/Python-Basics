'''Using class and objects in python, write a program to get the real and imaginary part of
two real numbers. Get the real and imaginary part of one complex number from user and
for second one set yourself.'''
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        print(f"{self.real} + {self.imag}i")

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
real = int(input("Enter real part of first complex number: "))
imag = int(input("Enter imaginary part of first complex number: "))
c1 = ComplexNumber(real, imag)
c2 = ComplexNumber(3, 4)

#Using instance function display those two complex numbers
print("First complex number:")
c1.display()
print("Second complex number:")
c2.display()

'''Using different instance function, find the sum, difference and multiplication of those two
complex number, get that stored in another number and use the function created in
previous part to show the result.'''
sum_result = c1.add(c2)
diff_result = c1.subtract(c2)
prod_result = c1.multiply(c2)
print("Sum of the two complex numbers:")
sum_result.display()
print("Difference of the two complex numbers:")
diff_result.display()
print("Product of the two complex numbers:")
prod_result.display()
