#opening file in read and write mode
f1=open("file1.txt","r+")
#writing the string 'hello world'
f1.write("\nHello world")
#reading the line from the file
temp=f1.readline()
print(temp)
