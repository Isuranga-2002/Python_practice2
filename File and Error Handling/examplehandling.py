#read()
file = open("diaries.txt", "r")
content = file.read()
print(content)
file.close()
print(".......................")


#readline()
file = open("diaries.txt", "r")
line1 = file.readline()
line2 = file.readline()
print(line1)
print(line2)
file.close()
print(".......................")


#readlines()
file = open("diaries.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()
print(".......................")


#write()
file = open("diaries.txt", "w")
file.write("Hello, Python!\n")
file.write("File handling is easy.")
file.close()

file = open("diaries.txt", "r")
content = file.read()
print(content)
file.close()
print(".......................")


#writelines()
lines = ["First line\n", "Second line\n", "Third line\n"]
file = open("diaries.txt", "w")
file.writelines(lines)
file.close()

file = open("diaries.txt", "r")
content = file.read()
print(content)
file.close()
print(".......................")

#Appending data
file = open("diaries.txt", "a")
file.write("\nThis line is added later.")
file.close()

file = open("diaries.txt", "r")
content = file.read()
print(content)
file.close()
print(".......................")

#with statement
with open("diaries.txt", "r") as file:
    content = file.read()
    print(content)
print(".......................")

#File existence
import os

if os.path.exists("diaries.txt"):
    print("File found!")
else:
    print("File not found!")
print(".......................")

#Delete file
import os
os.remove("diaries.txt")
print("File was deleted successfully!")








