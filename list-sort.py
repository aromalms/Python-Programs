#Program to read a list of numbers and sort it without using a sort function
limit=int(input("Enter Limit: "))
num_list=[]
for i in range (0,limit):
    temp=input("Enter numbers: ")
    num_list.append(temp)
for i in range (0,limit-1):
    for j in range (0,limit-i-1):
        if (num_list[i]<num_list[j]):
            temp=num_list[i]
            num_list[i]=num_list[j]
            num_list[j]=temp
print(num_list)