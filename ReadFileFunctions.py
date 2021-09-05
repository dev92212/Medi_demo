file1 = open("Textfile.txt")
#print(file1.read())
#print((file1.readline()))
#print(file1.read(7) + file1.readline() + file1.readline())

# lines = " "
# while lines != "":
#     print(lines)
#     lines = file1.readline()

allLines = file1.readlines()
print(allLines[2])

file1.close()

### 2nd Method to read. --> BETTER <--
with open('Textfile.txt', 'r') as objFile:
    Alllines = objFile.readlines()
    print(Alllines)
