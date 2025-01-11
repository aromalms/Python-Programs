#To find facorial of a number
num=int(input("Enter Number: "))
fact=1
i=1
while i!=num+1:
    fact=fact*i
    i+=1
print(fact)