with open("Textfile.txt", 'r') as objRead:
    filelist = objRead.readlines()
    print(filelist)
    with open("Textfile.txt", 'w') as objWrite:
        for i in reversed(filelist):
            objWrite.write(i)