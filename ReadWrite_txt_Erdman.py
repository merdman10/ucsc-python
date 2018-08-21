#Monica Erdman
#Aug. 15, 2018
#Reading and writing text files writing assignment 1

#1. Read file text1.txt and count the number of non-empty lines in the file. Use tell() to find the file pointer's position.
text1 = open('text1.txt','r')
l = 0
line = text1.readline()
while line:
    print(line[:-1], "\nPosition:",text1.tell())
    line = text1.readline()
text1.close()

#2. Write the following words in to a new file day1.txt: absolutely productive day
day1 = open('day1.txt','w')
day1.write("absolutely\n")
day1.write("productive\n")
day1.write("day\n")
day1.close()

#3. What is the difference between:
#a. read() and readlines() methods.
with open('text1.txt','r') as text:
    print("Using read() method:\n", text.read()) #reads and returns the whole file as a string
with open('text1.txt','r') as text:
    print("Using readlines() method:\n", text.readlines()) #reads the whole file, line by line, into a list

#b. Write and append access modes.

#write access mode creates a file (if it doesn't exist), writes to it, and overwrites it (if it does exist)
#Append access mode also writes to a file by appending to it, does not overwrite, and creates a file if it doesn't exist


#4. Open a new file called new1.txt and write lines: new operator; new findings; new text; and then seek() and read all the lines.
with open('new1.txt','w+') as new:
    new.write("new operator\n")
    new.write("new findings\n")
    new.write("new text")
    new.seek(0)
    print("Position:",new.tell())
    print(new.read())
