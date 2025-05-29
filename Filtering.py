#Use filter function that filters vowels from the list [a,e,d,f,g,t,I,c,w]
def is_vowel(char):
    return char.lower() in 'aeiou'

my_list = ['a', 'e', 'd', 'f', 'g', 't', 'I', 'c', 'w']
filtered_list = list(filter(is_vowel, my_list))
print(filtered_list)

#Use filter function and prints even list and odd numbers list less than 20.
numbers = list(range(1, 20))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
