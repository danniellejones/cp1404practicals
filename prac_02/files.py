"""
CP1401 | Prac_02 Files | Dannielle Jones
Program that shows different ways to read files: read(), readline(), readlines(), for line in file
"""

# 1. Asks user for their name, then opens file called "name.txt" and writes name to it
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2. Opens "name.txt" and reads the name then prints "Your name is ..."
in_file = open("name.txt", 'r')
name = in_file.read().strip()  # Assumes file "name.txt" will only contain one name
print("Your name is", name)
in_file.close()

# 3. Open "numbers.txt", read the first two numbers and adds them together, then print result
in_file = open("numbers.txt", 'r')
first_number = in_file.readline()
second_number = in_file.readline()
total = int(first_number) + int(second_number)
print(total)
in_file.close()

# 4. Prints the total for all lines in "numbers.txt" or a file with any number of numbers
in_file = open("numbers.txt", 'r')
result = 0
for line in in_file:
    result += int(line)
print(result)
in_file.close()
