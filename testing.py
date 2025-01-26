#Reading the Input
fileList=input("Enter Names (separated by comma): ").split(',')
#Reading the string to be compared
checkName=input("Enter the string to be compared: ")
for fileName in fileList:
    if checkName in fileName:
        print(fileName)