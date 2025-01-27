#read n number of elements into an array, if the value is positive put it in an array, otherwise in another
n=int(input("Enter limit:"))
list1=[]
positive=[]
negative=[]
for i in range(0,n):
    val=int(input("Enter Number: "))
    list1.append(val)
print(list1)
for j in list1:
    if(j>0):
        positive.append(j)
    else:
        negative.append(j)
print(positive)
print(negative)