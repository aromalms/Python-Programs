#Fibonacci series
limit=int(input("Enter limit: "))
x=0
y=1
list1=[]
for i in range(0,limit):
    print(x)
    temp=x
    x=y
    y=y+temp
