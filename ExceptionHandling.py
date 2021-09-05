items = 0

if items !=2:
    #raise Exception("Test failed. Card empty!")
    pass

#assert (items == 1), "Failed"


### Try - Catch blocks
try:
    with open("Textfile2.txt", 'r') as readObj:
        print(readObj.readline())

except Exception as ex:
    print("ERROR-->", ex)

finally:
    print("End of execution. Cleaning resources. Logs ended.")