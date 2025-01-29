#to count the frequency of each word in a string using dictionary
s="Hello Hello Good Morning Morning Morning Morning Morning"
dict={}
i=1
for str in s.split():
    if str in dict:
        i=i+1
        dict[str]=i
    else:
        i=1
        dict[str]=i
print(dict)