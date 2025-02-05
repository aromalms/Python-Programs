#counting the occurences of each character in a string and forming a dictionary with character as the key
str="Heellllllllllo Good"
dict={}
for i in str:
    dict[i]=0
for i in str:
    dict[i]+=1
print(dict)