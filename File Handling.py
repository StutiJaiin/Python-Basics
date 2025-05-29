#Create a file (your_name.text) and write about your-self in that file through file handling function. Save at least 10 lines
lines = [
    "My name is Stuti.\n",
    "I am a studying computer science.\n",
    "I like to code.\n",
    "Porgramming in python.\n",
    "Python Programming.\n",
    "Helps in.\n",
    "Problem Solving.\n",
    "and Data Science.\n",
    "Data Strcutures and Algorithms.\n",
    "is a little hard.\n"
]

with open("stuti.txt", "w") as file:
    file.writelines(lines)

#Display the content of file (your_name.text) line by line.
with open("stuti.txt", "r") as file:
    for line in file:
        print(line.strip())


#Display the number of lines in file (your_name.text) which are not starting with alphabet “A”.
count = 0
with open("stuti.txt", "r") as file:
    for line in file:
        if not line.strip().startswith('A'):
            count += 1
print("Lines not starting with 'A':", count)



#Display the total number of words in file (your_name.text).
with open("stuti.txt", "r") as file:
    text = file.read()
    words = text.split()
    print("Total words:", len(words))


#Display the count of those words whose length is less than 4 in file (your_name.text)
with open("stuti.txt", "r") as file:
    text = file.read()
    words = text.split()
    short_words = [word for word in words if len(word) < 4]
    print("Words with length less than 4:", len(short_words))
